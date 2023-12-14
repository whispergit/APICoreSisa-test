import requests

# GET /Students/GetStudents
# GET /Students/GetStudent/{id}
# GET /Students/GetQuestion/{id}
# GET /Students/GetRequest/{id}
# GET /Students/checkGrade


def test_get_students(s: requests.Session):
    route = '/Students/GetStudents'

    # 200

    r = s.get(
        route,
    )

    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)


def test_get_student_id(s: requests.Session):
    route = '/Students/GetStudent/{id}'

    # get all

    r = s.get(
        '/Students/GetStudents',
    )

    assert r.status_code == 200
    db_data = r.json()

    # 200

    r = s.get(
        route.format(id=105),
    )

    assert r.status_code == 200
    data = r.json()
    assert data in db_data

    # 404

    r = s.get(
        route.format(id=10000000),
    )

    assert r.status_code == 404


def test_get_question_id(s: requests.Session):
    route = '/Students/GetQuestion/{id}'

    # 200

    r = s.get(
        route.format(id=5670010718),
    )

    assert r.status_code == 200

    # 404

    r = s.get(
        route.format(id=0),
    )


def test_get_request_id(s: requests.Session):
    route = '/Students/GetRequest/{id}'

    # 200

    r = s.get(
        route.format(id=5670010718),
    )

    assert r.status_code == 200

    # 404

    r = s.get(
        route.format(id=0),
    )


def test_check_grade(s: requests.Session):
    route = '/Students/checkGrade/{id}'

    # 200

    r = s.get(
        route.format(id=5670010718),
    )

    assert r.status_code == 200
    data = r.json()
    assert data == False

    # 404

    r = s.get(
        route.format(id=0),
    )

    assert r.status_code == 404
