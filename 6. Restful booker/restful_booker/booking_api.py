from requests import Response, Session

from restful_booker.config import BASE_URL
from restful_booker.models import Booking


class BookingApi:
    def __init__(self, session: Session):
        self.session = session
        self.url = f"{BASE_URL}/booking"

    def get_booking_ids(self) -> Response:
        return self.session.get(self.url)

    def get_booking(self, booking_id: int, accept: str | None = None) -> Response:
        if accept:
            headers = {
                "Accept": accept,
            }
        else:
            headers = None

        return self.session.get(f"{self.url}/{booking_id}", headers=headers)

    def create_booking(self, booking: Booking) -> Response:
        return self.session.post(self.url, json=booking.model_dump(mode="json"))

    def update_booking(self, booking_id: int, booking: Booking, token: str) -> Response:
        return self.session.put(
            f"{self.url}/{booking_id}",
            json=booking.model_dump(mode="json"),
            headers={
                "Cookie": f"token={token}",
            },
        )

    def delete_booking(self, booking_id: int, token: str) -> Response:
        return self.session.delete(
            f"{self.url}/{booking_id}",
            headers={
                "Cookie": f"token={token}",
            },
        )
