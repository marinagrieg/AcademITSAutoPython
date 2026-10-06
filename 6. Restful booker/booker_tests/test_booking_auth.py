import allure

from restful_booker.config import PASSWORD, USERNAME
from restful_booker.models import Auth, AuthResponse


@allure.epic("Booking API")
@allure.feature("Authentication")
@allure.story("Positive Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Авторизация с валидными данными")
def test_auth_returns_token(auth_api):
    response = auth_api.create_token(Auth(username=USERNAME, password=PASSWORD))

    assert response.status_code == 200
    assert AuthResponse.model_validate(response.json()).token


@allure.epic("Booking API")
@allure.feature("Authentication")
@allure.story("Negative Authentication")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Авторизация с невалидным паролем")
def test_auth_with_invalid_password_returns_bad_credentials(auth_api):
    response = auth_api.create_token(Auth(username=USERNAME, password="invalid-password"))

    assert response.json() == {
        "reason": "Bad credentials",
    }
