import pytest
import requests

from tests.constants import BASE, HEADERS, SSL_VERIFY

# GET /Questioniars/GetQuestioniars
# GET /Questioniars/GetQuestioniar/{id}
# POST /Questioniars/UploadImage/upload
# PUT /Questioniars/PutQuestioniar/{id}
# POST /Questioniars/PostQuestioniar
# PUT /Questioniars/InactiveQuestioniar/{id}


def test_get_questioniars():
    with requests.Session() as s:
        route = f"{BASE}/Questioniars/GetQuestioniars"

        # 200

        r = s.get(
            route,
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200
        data = r.json()
        for i in data:
            assert 'questId' in i
            assert 'questTopic' in i
            assert 'questDescription' in i
            assert 'questUpload' in i
            assert 'questLink' in i
            assert 'questTerm' in i
            assert 'questType' in i
            assert 'questDepartment' in i
            assert 'questStatus' in i
            assert 'questCreateDate' in i
            assert 'questDateStart' in i
            assert 'questDateEnd' in i
            assert 'questCreateBy' in i
            assert 'qeustDiploma' in i
            assert 'questBachelor' in i
            assert 'questMaster' in i
            assert 'questDoctor' in i


def test_get_questioniar_id():
    with requests.Session() as s:
        route = "{base}/Questioniars/GetQuestioniar/{id}"

        # get all

        r = s.get(
            f"{BASE}/Questioniars/GetQuestioniars",
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200
        db_data = r.json()

        # 200

        for i in db_data:
            queue_id = i["questId"]
            r = s.get(
                route.format(base=BASE, id=queue_id),
                headers=HEADERS,
                verify=SSL_VERIFY,
            )

            assert r.status_code == 200
            data = r.json()
            assert data == i

        # 404

        r = s.get(
            route.format(base=BASE, id=0),
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 404


def test_post_upload_image():
    with requests.Session() as s:
        route = "{base}/Questioniars/UploadImage/upload?id={id}"

        # get all

        r = s.get(
            f"{BASE}/Questioniars/GetQuestioniars",
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200
        db_data = r.json()

        # 200

        for q in db_data:
            r = s.post(
                route.format(base=BASE, id=q['questId']),
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
                route.format(base=BASE, id=q['questId']),
                headers=HEADERS,
                verify=SSL_VERIFY,
            )

            assert r.status_code == 400
            break


def test_put_questioniar_id():
    with requests.Session() as s:
        route = "{base}/Questioniars/PutQuestioniar/{id}"

        # get all

        r = s.get(
            f"{BASE}/Questioniars/GetQuestioniars",
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200
        db_data = r.json()

        # 200
        payload = {}
        for payload in db_data:
            r = s.put(
                route.format(base=BASE, id=payload['questId']),
                headers=HEADERS,
                verify=SSL_VERIFY,
                json=payload,
            )

            assert r.status_code == 204
            break

        # 404

        payload['questId'] = 0
        r = s.put(
            route.format(base=BASE, id=payload['questId']),
            headers=HEADERS,
            verify=SSL_VERIFY,
            json=payload,
        )

        assert r.status_code == 404


def test_post_questioniar():
    with requests.Session() as s:
        route = f"{BASE}/Questioniars/PostQuestioniar"

        payload = {"questTopic": "string"}

        r = s.post(
            route,
            headers=HEADERS,
            verify=SSL_VERIFY,
            json=payload,
        )

        assert r.status_code == 201
        # data = r.json()


@pytest.mark.skip(reason="this route is not used")
def test_put_inactive_questioniar_id():
    with requests.Session() as s:
        route = "{base}/Questioniars/InactiveQuestioniar/{id}"

        r = s.put(
            route.format(base=BASE, id=12),
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200

        # fetch again

        r = s.get(
            "{base}/Questioniars/GetQuestioniar/{id}".format(base=BASE, id=12),
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200

        data = r.json()
        assert data["questStatus"] in ["Inactive", "string"]
