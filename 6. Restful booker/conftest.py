from datetime import date

import pytest
from requests import Session

from restful_booker.auth_api import AuthApi
from restful_booker.booking_api import BookingApi
from restful_booker.config import PASSWORD, USERNAME
from restful_booker.models import Auth, AuthResponse, Booking, BookingDates, BookingResponse


@pytest.fixture(scope="session")
def http_session():
    with Session() as session:
        session.headers["Accept"] = "application/json"
        yield session


@pytest.fixture(scope="session")
def auth_api(http_session):
    return AuthApi(http_session)


@pytest.fixture(scope="session")
def booking_api(http_session):
    return BookingApi(http_session)


@pytest.fixture(scope="session")
def token(auth_api):
    response = auth_api.create_token(Auth(username=USERNAME, password=PASSWORD))
    assert response.status_code == 200, response.text

    return AuthResponse.model_validate(response.json()).token


@pytest.fixture
def booking_payload():
    return Booking(
        firstname="Mary",
        lastname="White",
        totalprice=200,
        depositpaid=True,
        bookingdates=BookingDates(
            checkin=date(2026, 10, 10),
            checkout=date(2026, 10, 12)
        ),
        additionalneeds="Breakfast",
    )


@pytest.fixture
def created_booking(booking_api, booking_payload, token):
    response = booking_api.create_booking(booking_payload)
    assert response.status_code == 200, response.text
    created = BookingResponse.model_validate(response.json())

    yield created

    booking_api.delete_booking(created.bookingid, token)
