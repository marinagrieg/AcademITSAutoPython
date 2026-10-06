import allure

@allure.epic("Booking API")
@allure.feature("Get Bookings")
@allure.story("Status Code")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Получение списка бронирований")
def test_get_booking_ids_returns_200(booking_api):
    response = booking_api.get_booking_ids()

    assert response.status_code == 200


@allure.epic("Booking API")
@allure.feature("Get Booking by Id")
@allure.story("Status Code")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Получение бронирования по Id")
def test_get_booking_returns_200(booking_api, created_booking):
    response = booking_api.get_booking(created_booking.bookingid)

    assert response.status_code == 200

@allure.epic("Booking API")
@allure.feature("Get Booking by Id")
@allure.story("Status Code")
@allure.severity(allure.severity_level.MINOR)
@allure.title("Получение бронирования по Id с невалидным media type")
def test_get_booking_with_bad_accept_returns_418(booking_api, created_booking):
    response = booking_api.get_booking(created_booking.bookingid, accept="text/plain")

    assert response.status_code == 418

@allure.epic("Booking API")
@allure.feature("Post Booking")
@allure.story("Status Code")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Создание бронирования с валидными данными")
def test_create_booking_returns_200(booking_api, booking_payload):
    response = booking_api.create_booking(booking_payload)

    assert response.status_code == 200


@allure.epic("Booking API")
@allure.feature("Delete Booking by Id")
@allure.story("Status Code")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Удаление бронирования по Id")
def test_delete_booking_returns_201(booking_api, created_booking, token):
    response = booking_api.delete_booking(created_booking.bookingid, token)

    assert response.status_code == 201
