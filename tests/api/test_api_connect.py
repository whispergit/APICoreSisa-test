import requests

from tests.constants import BASE, HEADERS, SSL_VERIFY


def test_post_connect_users_login():
    with requests.Session() as s:
        route = f"{BASE}/APIConnect/UserLogin"

        # 200
        r = s.post(
            route,
            json={
                "username": "admin2",
                "password": "admin2",
            },
            verify=SSL_VERIFY,
        )
        assert r.status_code == 200

        data = r.json()
        assert data["id"] == 2
        assert data["roleId"] == 5
        assert data["name"] == "admin2"
        assert data["email"] == "admin2@voutlook.com"
        assert data["username"] == "admin2"
        assert data["password"] == "admin2"
        assert data["status"] == True
        assert data["lastUpdate"] == "2021-08-31T16:01:05.4581518"
        assert data["tel"] == "-"
        assert data["departments"] is None
        assert data["department"] is None
        assert data["role"] is None

        # 404

        r = s.post(
            route,
            json={
                "username": "admin2",
                "password": "admin",
            },
            verify=SSL_VERIFY,
        )

        assert r.status_code == 404

        # without password

        r = s.post(
            route,
            json={
                "username": "admin2",
            },
            verify=SSL_VERIFY,
        )

        assert r.status_code == 400

        # without username

        r = s.post(
            route,
            json={
                "password": "admin",
            },
            verify=SSL_VERIFY,
        )

        assert r.status_code == 400


def test_post_connect_students_login():
    with requests.Session() as s:
        route = f"{BASE}/APIConnect/StudentLogin"

        # 200
        r = s.post(
            route,
            headers=HEADERS,
            json={
                "code": "5670010718",
            },
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200
        data = r.json()
        assert data["id"] == 105
        assert data["code"] == "5670010718"
        assert data["name"] == "นายทดสอบ  19:26"
        assert data["eduId"] == 1
        assert data["card"] == "0500489036878"
        assert data["passportId"] is None
        assert data["mobile"] == "0884050958"
        assert data["email"] == "lungdin@gmail.com "  # with space why?
        assert data["password"] == "751753d46467270b9ef9d329a6745ad3"
        assert data["active"] == 1
        assert data["lastUpdate"] == "2021-01-25T13:40:52.0805212"
        assert data["confirmCode"] == "fdb4a8fb74f40a6c786d542deb2b260d"
        assert data["firstLogin"] == 1
        assert data["createDate"] == "2021-01-25T13:40:52.0805212"

        # 404

        r = s.post(
            route,
            headers=HEADERS,
            json={
                "code": "101213135",
            },
            verify=SSL_VERIFY,
        )

        assert r.status_code == 404
