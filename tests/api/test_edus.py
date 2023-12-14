import pytest
import requests


@pytest.mark.skip(reason='this route is not used')
def test_get_edus(s: requests.Session):
    route = '/Edus/GetEdus'

    # 200

    r = s.get(
        route,
    )

    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)


@pytest.mark.skip(reason='this route is not used')
def test_get_edu_id(s: requests.Session):
    route = '/Edus/GetEdu/{id}'

    # 200

    for edu_id in range(1, 5):
        r = s.get(
            route.format(id=edu_id),
        )

        assert r.status_code == 200
        data = r.json()
        assert data['id'] == edu_id
        # assert db_data[edu_id - 1]['name'] == data['name']
        # assert data['lastUpdate'] == '2019-01-01T00:00:00'

    # 404

    r = s.get(
        route.format(id=0),
    )

    assert r.status_code == 404
