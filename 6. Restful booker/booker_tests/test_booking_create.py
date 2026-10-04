from restful_booker.models import Booking, BookingResponse


def test_create_booking_returns_same_data(booking_api, booking_payload):
    response = booking_api.create_booking(booking_payload)

    assert response.status_code == 200

    created = BookingResponse.model_validate(response.json())

    assert created.booking == booking_payload

    fetched = booking_api.get_booking(created.bookingid)

    assert fetched.status_code == 200
    assert Booking.model_validate(fetched.json()) == booking_payload
