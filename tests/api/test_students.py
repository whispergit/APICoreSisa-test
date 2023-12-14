import requests

from tests.constants import BASE, HEADERS, SSL_VERIFY

# GET /Students/GetStudents
# GET /Students/GetStudent/{id}
# GET /Students/GetQuestion/{id}
# GET /Students/GetRequest/{id}
# GET /Students/checkGrade


def test_get_students():
    with requests.Session() as s:
        route = f"{BASE}/Students/GetStudents"

        # 200

        r = s.get(
            route,
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200
        data = r.json()
        assert isinstance(data, list)


def test_get_student_id():
    with requests.Session() as s:
        route = "{base}/Students/GetStudent/{id}"

        # get all

        r = s.get(
            f"{BASE}/Students/GetStudents",
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200
        db_data = r.json()

        # 200

        r = s.get(
            route.format(base=BASE, id=105),
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200
        data = r.json()
        assert data in db_data

        # 404

        r = s.get(
            route.format(base=BASE, id=10000000),
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 404


def test_get_question_id():
    with requests.Session() as s:
        route = "{base}/Students/GetQuestion/{id}"

        # 200

        r = s.get(
            route.format(base=BASE, id=5670010718),
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200

        # 404

        r = s.get(
            route.format(base=BASE, id=0),
            headers=HEADERS,
            verify=SSL_VERIFY,
        )


def test_get_request_id():
    with requests.Session() as s:
        route = "{base}/Students/GetRequest/{id}"

        # 200

        r = s.get(
            route.format(base=BASE, id=5670010718),
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200

        # 404

        r = s.get(
            route.format(base=BASE, id=0),
            headers=HEADERS,
            verify=SSL_VERIFY,
        )


def test_check_grade():
    with requests.Session() as s:
        route = "{base}/Students/checkGrade/{id}"

        # 200

        r = s.get(
            route.format(base=BASE, id=5670010718),
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200
        data = r.json()
        assert data == False

        # 404

        r = s.get(
            route.format(base=BASE, id=0),
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 404
