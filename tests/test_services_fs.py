import importlib
import json
import os
import stat
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


class HandshakeTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.token_path = Path(self.tempdir.name) / "credentials"
        os.environ["SOVEREIGN_TOKEN_STORE"] = str(self.token_path)
        import src.core.handshake as handshake
        self.handshake = importlib.reload(handshake)
        self.client = self.handshake.app.test_client()

    def tearDown(self):
        os.environ.pop("SOVEREIGN_TOKEN_STORE", None)
        self.tempdir.cleanup()

    def test_pin_is_six_alphanumeric_characters(self):
        self.assertRegex(self.handshake.PIN, r"^[A-Z0-9]{6}$")

    def test_pair_stores_token_with_private_permissions_and_is_single_use(self):
        response = self.client.post("/pair", json={"pin": self.handshake.PIN, "token": "scoped-token"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.token_path.read_text(), "scoped-token")
        self.assertEqual(stat.S_IMODE(self.token_path.stat().st_mode), 0o600)

        replay = self.client.post("/pair", json={"pin": self.handshake.PIN, "token": "other-token"})
        self.assertEqual(replay.status_code, 409)
        self.assertEqual(self.token_path.read_text(), "scoped-token")

    def test_invalid_and_missing_pairing_inputs_are_rejected(self):
        invalid = self.client.post("/pair", json={"pin": "WRONG1", "token": "secret"})
        self.assertEqual(invalid.status_code, 401)
        missing = self.client.post("/pair", json={"pin": self.handshake.PIN})
        self.assertEqual(missing.status_code, 400)

    def test_expired_pin_is_rejected(self):
        with patch.object(self.handshake, "PIN_EXPIRY", 0):
            response = self.client.post("/pair", json={"pin": self.handshake.PIN, "token": "secret"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json()["status"], "expired")


class PaeanBridgeTests(unittest.TestCase):
    def setUp(self):
        import src.core.handshake as handshake
        self.app = handshake.app
        self.client = self.app.test_client()
        self.root = Path(__file__).resolve().parents[1]

    def test_status_reports_root_pinned_sandbox(self):
        response = self.client.get("/paean/status")
        self.assertEqual(response.status_code, 200)
        body = response.get_json()
        self.assertEqual(body["bridge"], "active")
        self.assertEqual(body["sandbox"], "enabled — root only")

    def test_sync_writes_inside_root_and_blocks_traversal(self):
        safe_name = "tests/_sync_probe.txt"
        escape_name = "../../tmp/sovereign_escape_probe.txt"
        target = self.root / safe_name
        escaped = Path("/tmp/sovereign_escape_probe.txt")
        escaped.unlink(missing_ok=True)
        try:
            response = self.client.post(
                "/paean/sync",
                json={"files": {safe_name: "hello", escape_name: "blocked"}},
            )
            self.assertEqual(response.status_code, 200)
            body = response.get_json()
            self.assertIn(safe_name, body["files_written"])
            self.assertTrue(any(escape_name in item for item in body["skipped"]))
            self.assertEqual(target.read_text(), "hello")
            self.assertFalse(escaped.exists())
        finally:
            target.unlink(missing_ok=True)

    def test_sync_rejects_non_object_file_payload(self):
        response = self.client.post("/paean/sync", json={"files": ["not-a-map"]})
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
