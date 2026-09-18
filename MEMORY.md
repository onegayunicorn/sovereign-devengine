# Implementation Memory

- The repository supports Xbox retail hardware only through Xbox Dev Mode and UWP/MSIX sideloading; ordinary retail mode is not a supported execution target.
- Godot 3.5.3 UWP is the documented Dev Mode path. Godot 4 GDK guidance is for approved Xbox development environments and is not a replacement for Dev Mode sideloading.
- The Paean bridge is sandboxed to the repository root and must remain opt-in for deployment.
- Hardware, Xbox Device Portal, Gitea, and remote QPU access are never required by the offline test suite.
- `.env` and `~/.sovereign/credentials` are local secrets and must not be committed.
