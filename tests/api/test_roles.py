import pytest
import requests

# GET /Roles/GetRoles
# GET /Roles/GetRole/{id}


@pytest.mark.skip(reason='this route is not used')
def test_get_roles(s: requests.Session):
    route = '/Roles/GetRoles'

    # 200

    r = s.get(
        route,
    )

    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)


@pytest.mark.skip(reason='this route is not used')
def test_get_role_id(s: requests.Session):
    route = '/Roles/GetRole/{id}'

    # get all

    r = s.get(
        '/Roles/GetRoles',
    )

    assert r.status_code == 200
    db_data = r.json()

    # 200

    for role_id in range(0, 10):
        if role_id == 2 or role_id == 4:
            continue
        r = s.get(
            route.format(id=role_id),
        )

        assert r.status_code == 200, f'role_id: {role_id}'
        data = r.json()
        assert data in db_data
