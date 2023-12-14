import pytest
import requests

from tests.constants import BASE, HEADERS


@pytest.mark.skip(reason="this route is not used")
def test_get_edus():
    with requests.Session() as s:
        route = f"{BASE}/Edus/GetEdus"

        # 200

        r = s.get(
            route,
            headers=HEADERS,
        )

        assert r.status_code == 200
        data = r.json()
        assert isinstance(data, list)


@pytest.mark.skip(reason="this route is not used")
def test_get_edu_id():
    with requests.Session() as s:
        route = "{base}/Edus/GetEdu/{id}"

        # 200

        for edu_id in range(1, 5):
            r = s.get(
                route.format(base=BASE, id=edu_id),
                headers=HEADERS,
            )

            assert r.status_code == 200
            data = r.json()
            assert data["id"] == edu_id
            # assert db_data[edu_id - 1]["name"] == data["name"]
            # assert data["lastUpdate"] == "2019-01-01T00:00:00"

        # 404

        r = s.get(
            route.format(base=BASE, id=0),
            headers=HEADERS,
        )

        assert r.status_code == 404
