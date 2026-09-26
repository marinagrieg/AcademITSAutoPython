import pytest
import requests

BASE_URL = "https://reqres.in/api"


@pytest.fixture(scope="session")
def api():
    session = requests.Session()
    session.headers["x-api-key"] = "reqres-free-v1"

    return session


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture
def valid_payload():
    return {
        "email": "eve.holt@reqres.in",
        "password": "pistol",
    }