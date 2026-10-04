def test_get_booking_ids_returns_200(booking_api):
    response = booking_api.get_booking_ids()

    assert response.status_code == 200


def test_get_booking_returns_200(booking_api, created_booking):
    response = booking_api.get_booking(created_booking.bookingid)

    assert response.status_code == 200


def test_get_booking_with_bad_accept_returns_418(booking_api, created_booking):
    response = booking_api.get_booking(created_booking.bookingid, accept="text/plain")

    assert response.status_code == 418


def test_create_booking_returns_200(booking_api, booking_payload):
    response = booking_api.create_booking(booking_payload)

    assert response.status_code == 200


def test_delete_booking_returns_201(booking_api, created_booking, token):
    response = booking_api.delete_booking(created_booking.bookingid, token)

    assert response.status_code == 201
