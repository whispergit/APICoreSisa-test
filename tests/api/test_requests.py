import pytest
import requests

from tests.constants import BASE, HEADERS, SSL_VERIFY

# GET /Requests/GetRequests
# GET /Requests/GetRequest/{id}
# PUT /Requests/PutRequest/{id}
# POST /Requests/PostRequest
# POST /Requests/UploadImage/upload
# PUT /Requests/InactiveRequest/{id}


def test_get_requests():
    with requests.Session() as s:
        route = f"{BASE}/Requests/GetRequests"

        # 200

        r = s.get(
            route,
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200
        data = r.json()
        assert isinstance(data, list)


def test_get_request_id():
    with requests.Session() as s:
        route = "{base}/Requests/GetRequest/{id}"

        # get all

        r = s.get(
            f"{BASE}/Requests/GetRequests",
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200
        db_data = r.json()

        for req in db_data:
            req_id = req["requestId"]

            r = requests.get(
                route.format(base=BASE, id=req_id),
                headers=HEADERS,
                verify=SSL_VERIFY,
            )

            assert r.status_code == 200
            data = r.json()
            assert data == req


def test_put_request_id():
    with requests.Session() as s:
        route = "{base}/Requests/PutRequest/{id}"

        # get all
        r = s.get(
            f"{BASE}/Requests/GetRequests",
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200
        db_data = r.json()

        # 200
        payload = {}
        for payload in db_data:
            r = requests.put(
                route.format(base=BASE, id=payload['requestId']),
                headers=HEADERS,
                verify=SSL_VERIFY,
                json=payload,
            )

            assert r.status_code == 204
            break

        # 404
        payload['requestId'] = 0
        r = requests.put(
            route.format(base=BASE, id=payload['requestId']),
            headers=HEADERS,
            verify=SSL_VERIFY,
            json=payload,
        )

        assert r.status_code == 404


def test_post_request():
    with requests.Session() as s:
        route = f"{BASE}/Requests/PostRequest"

        # get all
        r = s.get(
            f"{BASE}/Requests/GetRequests",
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200
        db_data = r.json()

        for _, data in enumerate(db_data, start=1):
            data.pop("requestId")

            r = requests.post(
                route,
                json=data,
                headers=HEADERS,
                verify=SSL_VERIFY,
            )

            assert r.status_code == 201
            if _ >= 5:
                break


def test_post_upload_image():
    with requests.Session() as s:
        route = "{base}/Requests/UploadImage/upload?id={id}"

        # get id from db

        r = s.get(
            f"{BASE}/Requests/GetRequests",
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200
        db_data = r.json()

        # 200
        for q in db_data:
            r = s.post(
                route.format(base=BASE, id=q["requestId"]),
                headers=HEADERS,
                files={
                    "file": open("images/test.png", "rb"),
                },
                verify=SSL_VERIFY,
            )

            assert r.status_code == 200
            break

        # 404

        r = s.post(
            route.format(base=BASE, id=0),
            headers=HEADERS,
            files={
                "file": open("images/test.png", "rb"),
            },
            verify=SSL_VERIFY,
        )

        assert r.status_code == 404

        # 400

        for q in db_data:
            r = s.post(
                route.format(base=BASE, id=q["requestId"]),
                headers=HEADERS,
                verify=SSL_VERIFY,
            )

            assert r.status_code == 400
            break


@pytest.mark.skip(reason="this route is not used")
def test_put_inactive_request_id():
    with requests.Session() as s:
        route = "{base}/Requests/InactiveRequest/{id}"

        # 200

        r = s.put(
            route.format(base=BASE, id=1),
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200
        data = r.text
        assert data == "requrst"
        # TODO: what is this?
