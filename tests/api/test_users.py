import requests

from tests.constants import BASE, HEADERS, SSL_VERIFY

# GET / Users / GetUsers
# GET / Users / GetUser / {username}


def test_get_users():
    with requests.Session() as s:
        route = f"{BASE}/Users/GetUsers"

        # 200

        r = s.get(
            route,
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200
        data = r.json()

        for i in data:
            assert 'id' in i
            assert 'roleId' in i
            assert 'departmentId' in i
            assert 'name' in i
            assert 'email' in i
            assert 'username' in i
            assert 'password' in i
            assert 'status' in i
            assert 'lastUpdate' in i
            assert 'tel' in i
            assert 'departments' in i
            assert 'department' in i
            assert 'role' in i


def test_get_user_id():
    with requests.Session() as s:
        route = "{base}/Users/GetUser/{username}"

        # get all

        r = s.get(
            f"{BASE}/Users/GetUsers",
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200
        db_data = r.json()

        # 200

        for user in db_data:
            user_id = user["id"]
            user_username = user["username"]

            r = s.get(
                route.format(base=BASE, username=user_username),
                headers=HEADERS,
            )

            assert r.status_code == 200, f"User id: {user_id} - {user_username}"
            data = r.json()

            assert data["id"] == user["id"]
            assert data["roleId"] == user["roleId"]
            assert data["departmentId"] == user["departmentId"]
            assert data["name"] == user["name"]
            assert data["email"] == user["email"]
            assert data["username"] == user["username"]
            assert data["password"] == user["password"]
            assert data["status"] == user["status"]
            assert data["lastUpdate"] == user["lastUpdate"]
            assert data["tel"] == user["tel"]
            assert data["departments"] == user["departments"]
            assert data["department"] == user["department"]
            assert data["role"] == user["role"]

        # 404

        r = s.get(
            route.format(base=BASE, username="notfound"),
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 404
