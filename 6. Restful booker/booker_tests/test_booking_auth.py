from restful_booker.config import PASSWORD, USERNAME
from restful_booker.models import Auth, AuthResponse


def test_auth_returns_token(auth_api):
    response = auth_api.create_token(Auth(username=USERNAME, password=PASSWORD))

    assert response.status_code == 200
    assert AuthResponse.model_validate(response.json()).token


def test_auth_with_invalid_password_returns_bad_credentials(auth_api):
    response = auth_api.create_token(Auth(username=USERNAME, password="invalid-password"))

    assert response.json() == {
        "reason": "Bad credentials",
    }
