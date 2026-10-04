from requests import Response, Session

from restful_booker.config import BASE_URL
from restful_booker.models import Auth


class AuthApi:
    def __init__(self, session: Session):
        self.session = session
        self.url = f"{BASE_URL}/auth"

    def create_token(self, auth: Auth) -> Response:
        return self.session.post(self.url, json=auth.model_dump())
