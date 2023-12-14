import pytest
import requests

# GET /RoleMenus/GetRoleMenus
# GET /RoleMenus/GetRoleMenu/{id}


@pytest.mark.skip(reason='this route is removed')
def test_get_role_menus(s: requests.Session):
    route = '/RoleMenus/GetRoleMenus'

    # 200

    r = s.get(
        route,
    )

    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)


@pytest.mark.skip(reason='this route is removed')
def test_get_role_menu_id(s: requests.Session):
    route = '/RoleMenus/GetRoleMenu/{id}'

    # get all

    route = f'/RoleMenus/GetRoleMenus'

    # 200

    r = s.get(
        route,
    )

    assert r.status_code == 200
    get_all_data = r.json()

    # 200

    for role_id in range(1, 13):
        r = s.get(
            route.format(id=role_id),
        )

        assert r.status_code == 200
        data = r.json()
        for item in data:
            assert item in get_all_data

    # 404

    r = s.get(
        route.format(id=0),
    )

    assert r.status_code == 200  # TODO: ควรเป็น 404
