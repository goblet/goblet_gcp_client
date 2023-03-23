from goblet_gcp_client.client import get_default_project, get_default_location


class TestClient:
    def test_get_default_project(self, monkeypatch):
        monkeypatch.setenv("GOOGLE_PROJECT", "TEST")
        assert get_default_project() == "TEST"

    def test_get_default_location_environment_variable(self, monkeypatch, requests_mock):
        monkeypatch.setenv("GCLOUD_REGION", "TEST")
        requests_mock.get(
            "http://metadata.google.internal/computeMetadata/v1/instance/region",
            text="us-central2",
        )
        assert get_default_location() == "TEST"

    def test_get_default_location_metadata_service(self, monkeypatch, requests_mock):
        requests_mock.get(
            "http://metadata.google.internal/computeMetadata/v1/instance/region",
            text="us-central2",
        )
        assert get_default_location() == "us-central2"
