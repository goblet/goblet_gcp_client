# Goblet GCP Client

![PyPI](https://img.shields.io/pypi/v/goblet_gcp_client?color=blue&style=plastic)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/goblet_gcp_client?style=plastic)

 Goblet GCP Client is a util library with support for creating GCP resource clients, GCP integration tests, and other related utils.

## Getting started

To install run: 

`pip install goblet-gcp-client`

## Using a Client

```python
from goblet_gcp_client import Client

cloudfunction_client = Client(
    "cloudfunctions",
    "v1",
    calls="projects.locations.functions",
    parent_schema="projects/{project_id}/locations/{location_id}",
)

scheduler_client = Client(
    "cloudscheduler",
    "v1",
    calls="projects.locations.jobs",
    parent_schema="projects/{project_id}/locations/{location_id}",
)

# override default parent_key with "name"
cloudfunction_client.execute(
                "get", parent_key="name", parent_schema="projects/{project_id}/locations/{location_id}/functions/{name}"
            )

# pass in body params
sample_body = {}
resp = cloudfunction_client.execute(
                "patch",
                parent_key="name",
                parent_schema="projects/{project_id}/locations/{location_id}/functions/{name}",
                params={"body": sample_body},
            )

# Wait for previous operation to complete
cloudfunction_client.wait_for_operation(resp["name"], calls="operations")
```

## Writing Integration Tests:

Write your test and set env variable `G_HTTP_TEST` to `RECORD`

By default responses will be written to the `/tests/data` folder. You can customize this by setting `G_TEST_DATA_DIR` env variable.

Setting the `G_MOCK_CREDENTIALS` environment variable will use AnonymousCredentials. 

```python
def TestDeploy(self):
    monkeypatch.setenv("G_HTTP_TEST", "RECORD")
    monkeypatch.setenv("G_TEST_NAME", "TEST_NAME")

    cloudfunction_client = Client(
        "cloudfunctions",
        "v1",
        calls="projects.locations.functions",
        parent_schema="projects/{project_id}/locations/{location_id}",
    )

    cloudfunction_client.execute(
        "get", parent_key="name", parent_schema="projects/{project_id}/locations/{location_id}/functions/{name}"
    )
```
Running your test will record all responses that your Client makes

Now you can run your tests with `G_HTTP_TEST` with `REPLAY`. You can access the responses with `get_responses` or `get_response`

```python
from goblet_gcp_client import get_responses, get_response, get_replay_count

def TestDeploy(self):

    monkeypatch.setenv("G_HTTP_TEST", "REPLAY")
    monkeypatch.setenv("G_TEST_NAME", "TEST_NAME")

    cloudfunction_client = Client(
        "cloudfunctions",
        "v1",
        calls="projects.locations.functions",
        parent_schema="projects/{project_id}/locations/{location_id}",
    )
    cloudfunction_client.execute(
        "get", parent_key="name", parent_schema="projects/{project_id}/locations/{location_id}/functions/{name}"
    )

    responses = get_responses("TEST_NAME")
    assert len(responses) == 2
    assert "test_value" in responses[0]["body"]
    assert get_replay_count() == 1
```

## Features

* GCP resource clients
* GCP HTTP Test Recording and Replaying

## Examples

[Client and Testing Examples](https://github.com/goblet/goblet_gcp_client/blob/main/examples)


## Issues

Please file any issues, bugs or feature requests as an issue on our [GitHub](https://github.com/goblet/goblet_gcp_client/issues) page.

## Want to Contribute

If you would like to contribute to the library (e.g. by improving the documentation, solving a bug or adding a cool new feature) submit a [pull request](https://github.com/goblet/goblet_gcp_client/pulls).
