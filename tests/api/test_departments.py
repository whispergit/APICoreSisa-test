import requests

from tests.constants import BASE, HEADERS, SSL_VERIFY


def test_get_departments():
    with requests.Session() as s:
        route = f"{BASE}/Departments/GetDepartments"

        # 200

        r = s.get(
            route,
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200


def test_get_departments_id():
    with requests.Session() as s:
        route = "{base}/Departments/GetDepartment/{id}"

        # 200

        r = s.get(
            route.format(base=BASE, id=1),
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200
        data = r.json()
        assert data["id"] == 1
        assert data["name"] == "admin"
        assert data["pin"] == 2
        assert data["lastUpdate"] == "2019-01-01T00:00:00"
        assert data["users"] == []

        # 404

        r = s.get(
            route.format(base=BASE, id=0),
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 404
