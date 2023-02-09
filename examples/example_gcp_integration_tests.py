from goblet_gcp_client import get_response


# Example taken from goblet
def test_destroy_redis(self, monkeypatch):
    monkeypatch.setenv("GOOGLE_PROJECT", "goblet")
    monkeypatch.setenv("GOOGLE_LOCATION", "us-central1")
    monkeypatch.setenv("G_TEST_NAME", "redis-destroy")
    monkeypatch.setenv("G_HTTP_TEST", "REPLAY")

    # Class that uses Client
    redis = Redis("goblet-redis", resource={"name": "redis-test"})
    # Calls client.execute("delete")
    redis.destroy()

    delete_redis = get_response(
        "redis-destroy",
        "delete-v1-projects-goblet-locations-us-central1-instances-redis-test_1.json",
    )
    assert "redis-test" in delete_redis["body"]["metadata"]["target"]
