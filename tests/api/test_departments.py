import requests


def test_get_departments(s: requests.Session):
    route = '/Departments/GetDepartments'

    # 200

    r = s.get(
        route,
    )

    assert r.status_code == 200


def test_get_departments_id(s: requests.Session):
    route = '/Departments/GetDepartment/{id}'

    # 200

    r = s.get(
        route.format(id=1),
    )

    assert r.status_code == 200
    data = r.json()
    assert data['id'] == 1
    assert data['name'] == 'admin'
    assert data['pin'] == 2
    assert data['lastUpdate'] == '2019-01-01T00:00:00'
    assert data['users'] == []

    # 404

    r = s.get(
        route.format(id=0),
    )

    assert r.status_code == 404
