from datetime import date

from restful_booker.models import Booking, BookingDates


def test_update_booking_changes_all_fields(booking_api, created_booking, token):
    updated_payload = Booking(
        firstname="Maria",
        lastname="Belova",
        totalprice=300,
        depositpaid=False,
        bookingdates=BookingDates(
            checkin=date(2026, 12, 1),
            checkout=date(2027, 1, 5),
        ),
        additionalneeds="Late checkout",
    )
    assert updated_payload != created_booking.booking

    response = booking_api.update_booking(created_booking.bookingid, updated_payload, token)

    assert response.status_code == 200
    assert Booking.model_validate(response.json()) == updated_payload

    fetched = booking_api.get_booking(created_booking.bookingid)

    assert fetched.status_code == 200
    assert Booking.model_validate(fetched.json()) == updated_payload
