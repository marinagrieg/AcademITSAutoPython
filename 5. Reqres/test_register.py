import json


def test_register_content_type(api, base_url, valid_payload):
    response = api.post(base_url + "/register", json=valid_payload)

    print(f"\nStatus: {response.status_code}")
    print(f"Content-Type: {response.headers['Content-Type']}")

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"


def test_register_response_types(api, base_url, valid_payload):
    response = api.post(base_url + "/register", json=valid_payload)

    print(f"\nStatus: {response.status_code}")
    print(json.dumps(response.json(), indent=2))

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body["id"], int)
    assert isinstance(body["token"], str)
    assert body["token"] != ""


def test_register_no_password(api, base_url):
    payload = {
        "email": "eve.holt@reqres.in",
    }

    response = api.post(base_url + "/register", json=payload)

    print(f"\nStatus: {response.status_code}")
    print(json.dumps(response.json(), indent=2))

    assert response.status_code == 400
    assert response.json() == {"error": "Missing password"}


def test_register_unknown_email(api, base_url):
    payload = {
        "email": "unknown@reqres.in",
        "password": "1",
    }

    response = api.post(base_url + "/register", json=payload)

    print(f"\nStatus: {response.status_code}")
    print(json.dumps(response.json(), indent=2))

    assert response.status_code == 400
    assert response.json() == {"error": "Note: Only defined users succeed registration"}


# возвращает JSON с цветами и 200 вместо 405 на GET /register
def test_register_wrong_method(api, base_url):
    response = api.get(base_url + "/register")

    print(f"\nStatus: {response.status_code}")
    print(json.dumps(response.json(), indent=2))

    assert response.status_code == 405
    assert response.json() == {"error": "Method not allowed"}