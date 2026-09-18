import unittest

from services.qpu.stub_gateway import app, JOBS


class QpuGatewayTests(unittest.TestCase):
    def setUp(self):
        JOBS.clear()
        self.client = app.test_client()

    def test_local_backend_is_available(self):
        response = self.client.get("/qpu/backends")
        self.assertEqual(response.status_code, 200)
        body = response.get_json()
        self.assertEqual(body["backends"][0]["id"], "sim-local")
        self.assertTrue(body["backends"][0]["online"])

    def test_submit_and_fetch_job(self):
        response = self.client.post("/qpu/submit", json={"backend": "sim-local", "shots": 64})
        self.assertEqual(response.status_code, 200)
        job_id = response.get_json()["job_id"]
        result = self.client.get(f"/qpu/job/{job_id}")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.get_json()["shots"], 64)

    def test_unknown_job_returns_not_found(self):
        response = self.client.get("/qpu/job/missing")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
