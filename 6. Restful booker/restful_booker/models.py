from datetime import date

from pydantic import BaseModel


class Auth(BaseModel):
    username: str
    password: str


class AuthResponse(BaseModel):
    token: str


class BookingDates(BaseModel):
    checkin: date
    checkout: date


class Booking(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str | None = None


class BookingResponse(BaseModel):
    bookingid: int
    booking: Booking
