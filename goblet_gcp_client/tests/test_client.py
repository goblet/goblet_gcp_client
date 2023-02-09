from goblet_gcp_client.client import get_default_project, get_default_location


class TestClient:
    def test_get_default_project(self, monkeypatch):
        monkeypatch.setenv("GOOGLE_PROJECT", "TEST")
        assert get_default_project() == "TEST"

    def get_default_location(self, monkeypatch):
        monkeypatch.setenv("GCLOUD_REGION", "TEST")
        assert get_default_location() == "TEST"
