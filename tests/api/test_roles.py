import pytest
import requests

from tests.constants import BASE, HEADERS

# GET /Roles/GetRoles
# GET /Roles/GetRole/{id}


@pytest.mark.skip(reason="this route is not used")
def test_get_roles():
    with requests.Session() as s:
        route = f"{BASE}/Roles/GetRoles"

        # 200

        r = s.get(
            route,
            headers=HEADERS,
        )

        assert r.status_code == 200
        data = r.json()
        assert isinstance(data, list)


@pytest.mark.skip(reason="this route is not used")
def test_get_role_id():
    with requests.Session() as s:
        route = "{base}/Roles/GetRole/{id}"

        # get all

        r = s.get(
            f"{BASE}/Roles/GetRoles",
            headers=HEADERS,
        )

        assert r.status_code == 200
        db_data = r.json()

        # 200

        for role_id in range(0, 10):
            if role_id == 2 or role_id == 4:
                continue
            r = s.get(
                route.format(base=BASE, id=role_id),
                headers=HEADERS,
            )

            assert r.status_code == 200, f'role_id: {role_id}'
            data = r.json()
            assert data in db_data
