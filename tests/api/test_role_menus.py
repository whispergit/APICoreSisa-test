import pytest
import requests

from tests.constants import BASE, HEADERS

# GET /RoleMenus/GetRoleMenus
# GET /RoleMenus/GetRoleMenu/{id}


@pytest.mark.skip(reason="this route is removed")
def test_get_role_menus():
    with requests.Session() as s:
        route = f"{BASE}/RoleMenus/GetRoleMenus"

        # 200

        r = s.get(
            route,
            headers=HEADERS,
        )

        assert r.status_code == 200
        data = r.json()
        assert isinstance(data, list)


@pytest.mark.skip(reason="this route is removed")
def test_get_role_menu_id():
    with requests.Session() as s:
        route = "{base}/RoleMenus/GetRoleMenu/{id}"

        # get all

        route = f"{BASE}/RoleMenus/GetRoleMenus"

        # 200

        r = s.get(
            route,
            headers=HEADERS,
        )

        assert r.status_code == 200
        get_all_data = r.json()

        # 200

        for role_id in range(1, 13):
            r = s.get(
                route.format(base=BASE, id=role_id),
                headers=HEADERS,
            )

            assert r.status_code == 200
            data = r.json()
            for item in data:
                assert item in get_all_data

        # 404

        r = s.get(
            route.format(base=BASE, id=0),
            headers=HEADERS,
        )

        assert r.status_code == 200  # TODO: ควรเป็น 404
