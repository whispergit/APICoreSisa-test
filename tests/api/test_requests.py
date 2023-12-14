import pytest
import requests

# GET /Requests/GetRequests
# GET /Requests/GetRequest/{id}
# PUT /Requests/PutRequest/{id}
# POST /Requests/PostRequest
# POST /Requests/UploadImage/upload
# PUT /Requests/InactiveRequest/{id}


def test_get_requests(s: requests.Session):
    route = f'/Requests/GetRequests'

    # 200

    r = s.get(
        route,
    )

    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)


def test_get_request_id(s: requests.Session):
    route = '/Requests/GetRequest/{id}'

    # get all

    r = s.get(
        '/Requests/GetRequests',
    )

    assert r.status_code == 200
    db_data = r.json()

    for req in db_data:
        req_id = req['requestId']

        r = s.get(
            route.format(id=req_id),
        )

        assert r.status_code == 200
        data = r.json()
        assert data == req


def test_put_request_id(s: requests.Session):
    route = '/Requests/PutRequest/{id}'

    # get all
    r = s.get(
        f'/Requests/GetRequests',
    )

    assert r.status_code == 200
    db_data = r.json()

    # 200
    payload = {}
    for payload in db_data:
        r = s.put(
            route.format(id=payload['requestId']),
            json=payload,
        )

        assert r.status_code == 204
        break

    # 404
    payload['requestId'] = 0
    r = s.put(
        route.format(id=payload['requestId']),
        json=payload,
    )

    assert r.status_code == 404


def test_post_request(s: requests.Session):
    route = '/Requests/PostRequest'

    # get all
    r = s.get('/Requests/GetRequests')

    assert r.status_code == 200
    db_data = r.json()

    for _, data in enumerate(db_data, start=1):
        data.pop('requestId')

        r = s.post(
            route,
            json=data,
        )

        assert r.status_code == 201
        if _ >= 5:
            break


def test_post_upload_image(s: requests.Session):
    route = '/Requests/UploadImage/upload?id={id}'

    # get id from db

    r = s.get(
        '/Requests/GetRequests',
    )

    assert r.status_code == 200
    db_data = r.json()

    # 200
    for q in db_data:
        r = s.post(
            route.format(id=q['requestId']),
            files={
                'file': open('images/test.png', 'rb'),
            },
        )

        assert r.status_code == 200
        break

    # 404

    r = s.post(
        route.format(id=0),
        files={
            'file': open('images/test.png', 'rb'),
        },
    )

    assert r.status_code == 404

    # 400

    for q in db_data:
        r = s.post(
            route.format(id=q['requestId']),
        )

        assert r.status_code == 400
        break


@pytest.mark.skip(reason='this route is not used')
def test_put_inactive_request_id(s: requests.Session):
    route = '/Requests/InactiveRequest/{id}'

    # 200

    r = s.put(
        route.format(id=1),
    )

    assert r.status_code == 200
    data = r.text
    assert data == 'requrst'
    # TODO: what is this?
