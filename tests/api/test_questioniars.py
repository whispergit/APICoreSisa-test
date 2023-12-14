import pytest
import requests

# GET /Questioniars/GetQuestioniars
# GET /Questioniars/GetQuestioniar/{id}
# POST /Questioniars/UploadImage/upload
# PUT /Questioniars/PutQuestioniar/{id}
# POST /Questioniars/PostQuestioniar
# PUT /Questioniars/InactiveQuestioniar/{id}


def test_get_questioniars(s: requests.Session):
    route = '/Questioniars/GetQuestioniars'

    # 200

    r = s.get(
        route,
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


def test_get_questioniar_id(s: requests.Session):
    route = '/Questioniars/GetQuestioniar/{id}'

    # get all

    r = s.get(
        '/Questioniars/GetQuestioniars',
    )

    assert r.status_code == 200
    db_data = r.json()

    # 200

    for i in db_data:
        queue_id = i['questId']
        r = s.get(
            route.format(id=queue_id),
        )

        assert r.status_code == 200
        data = r.json()
        assert data == i

    # 404

    r = s.get(
        route.format(id=0),
    )

    assert r.status_code == 404


def test_post_upload_image(s: requests.Session):
    route = '/Questioniars/UploadImage/upload?id={id}'

    # get all

    r = s.get('/Questioniars/GetQuestioniars')

    assert r.status_code == 200
    db_data = r.json()

    # 200

    for q in db_data:
        r = s.post(
            route.format(id=q['questId']),
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
            route.format(id=q['questId']),
        )

        assert r.status_code == 400
        break


def test_put_questioniar_id(s: requests.Session):
    route = '/Questioniars/PutQuestioniar/{id}'

    # get all

    r = s.get(
        '/Questioniars/GetQuestioniars',
    )

    assert r.status_code == 200
    db_data = r.json()

    # 200
    payload = {}
    for payload in db_data:
        r = s.put(
            route.format(id=payload['questId']),
            json=payload,
        )

        assert r.status_code == 204
        break

    # 404

    payload['questId'] = 0
    r = s.put(
        route.format(id=payload['questId']),
        json=payload,
    )

    assert r.status_code == 404


def test_post_questioniar(s: requests.Session):
    route = f'/Questioniars/PostQuestioniar'

    payload = {'questTopic': 'string'}

    r = s.post(
        route,
        json=payload,
    )

    assert r.status_code == 201
    # data = r.json()


@pytest.mark.skip(reason='this route is not used')
def test_put_inactive_questioniar_id(s: requests.Session):
    route = '/Questioniars/InactiveQuestioniar/{id}'

    r = s.put(
        route.format(id=12),
    )

    assert r.status_code == 200

    # fetch again

    r = s.get(
        '/Questioniars/GetQuestioniar/{id}'.format(id=12),
    )

    assert r.status_code == 200

    data = r.json()
    assert data['questStatus'] in ['Inactive', 'string']
