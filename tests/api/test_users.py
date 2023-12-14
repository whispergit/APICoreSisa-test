import requests

# GET / Users / GetUsers
# GET / Users / GetUser / {username}


def test_get_users(s: requests.Session):
    route = '/Users/GetUsers'

    # 200

    r = s.get(
        route,
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


def test_get_user_id(s: requests.Session):
    route = '/Users/GetUser/{username}'

    # get all

    r = s.get(
        '/Users/GetUsers',
    )

    assert r.status_code == 200
    db_data = r.json()

    # 200

    for user in db_data:
        user_id = user['id']
        user_username = user['username']

        r = s.get(
            route.format(username=user_username),
        )

        assert r.status_code == 200, f'User id: {user_id} - {user_username}'
        data = r.json()

        assert data['id'] == user['id']
        assert data['roleId'] == user['roleId']
        assert data['departmentId'] == user['departmentId']
        assert data['name'] == user['name']
        assert data['email'] == user['email']
        assert data['username'] == user['username']
        assert data['password'] == user['password']
        assert data['status'] == user['status']
        assert data['lastUpdate'] == user['lastUpdate']
        assert data['tel'] == user['tel']
        assert data['departments'] == user['departments']
        assert data['department'] == user['department']
        assert data['role'] == user['role']

    # 404

    r = s.get(
        route.format(username='notfound'),
    )

    assert r.status_code == 404
