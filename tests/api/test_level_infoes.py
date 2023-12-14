import requests


def test_get_edu_level_for_infos(s: requests.Session):
    route = '/EduLevelForInfoes/GetEduLevelForInfos'

    # 200

    r = s.get(
        route,
    )

    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)


def test_get_edu_level_for_infos_id(s: requests.Session):
    route = '/EduLevelForInfoes/GetEduLevelForInfo/{id}'

    # get all

    r = s.get('/EduLevelForInfoes/GetEduLevelForInfos')

    assert r.status_code == 200
    db_data = r.json()

    # 200

    for edu_id in range(1, len(db_data)):
        r = s.get(
            route.format(id=edu_id),
        )

        assert r.status_code == 200
        data = r.json()
        assert data['id'] == edu_id
        assert db_data[edu_id - 1]['name'] == data['name']
        assert data['lastUpdate'] == '2019-01-01T00:00:00'

    # 404

    r = s.get(
        route.format(id=0),
    )

    assert r.status_code == 404
