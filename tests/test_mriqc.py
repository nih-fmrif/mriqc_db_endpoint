import pytest
from mriqc import mriqc


@pytest.fixture
def client(request):
    mriqc.app.config["TESTING"] = True
    client = mriqc.app.test_client()
    return client
