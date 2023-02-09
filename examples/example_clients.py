from goblet_gcp_client import Client

# Cloudfunction Examples
cloudfunction_client = Client(
    "cloudfunctions",
    "v1",
    calls="projects.locations.functions",
    parent_schema="projects/{project_id}/locations/{location_id}",
)

# override default parent_key with "name"
cloudfunction_client.execute(
    "get",
    parent_key="name",
    parent_schema="projects/{project_id}/locations/{location_id}/functions/{name}",
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
