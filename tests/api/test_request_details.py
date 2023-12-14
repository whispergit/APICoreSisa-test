import requests

from tests.constants import BASE, HEADERS, SSL_VERIFY

# GET / /GetRequestDetails
# GET /RequestDetails/GetRequestDetail/{id}
# POST /RequestDetails/PostRequestDetail
# GET /RequestDetails/GetReqStuDetail/{id}
# GET /RequestDetails/GetCountDetail/{id}


def test_get_request_details():
    with requests.Session() as s:
        route = f"{BASE}/RequestDetails/GetRequestDetails"

        # 200

        r = s.get(
            route,
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200
        # data = r.json()
        # assert data == []


def test_get_request_detail_id():
    with requests.Session() as s:
        route = "{base}/RequestDetails/GetRequestDetail/{id}"

        # 200

        # r = s.get(
        #     route.format(base=BASE, id=12),
        #     headers=HEADERS,
        #     verify=SSL_VERIFY,
        # )

        # assert r.status_code == 200

        # 400


def test_post_request_detail():
    with requests.Session() as s:
        route = f"{BASE}/RequestDetails/PostRequestDetail"

        payload = {
            "reqDId": 0,
            "reqDRequestid": 0,
            "reqDStuId": 105,
            "reqDDate": "2023-12-13T12:23:27.358Z",
        }

        r = s.post(
            route,
            headers=HEADERS,
            json=payload,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200

        # 404

        r = s.post(
            route,
            headers=HEADERS,
            json={},
            verify=SSL_VERIFY,
        )

        assert r.status_code == 404


def test_get_req_stu_detail_id():
    with requests.Session() as s:
        route = "{base}/RequestDetails/GetReqStuDetail/{id}"

        # 200

        r = s.get(
            route.format(base=BASE, id=1),
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200
        assert isinstance(r.json(), list)


def test_get_count_detail_id():
    with requests.Session() as s:
        route = "{base}/RequestDetails/GetCountDetail/{id}"

        # 200

        r = s.get(
            route.format(base=BASE, id=1),
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200
        assert isinstance(r.json(), int)
