import requests

from tests.constants import BASE, HEADERS, SSL_VERIFY


def test_get_edu_level_for_infos():
    with requests.Session() as s:
        route = f"{BASE}/EduLevelForInfoes/GetEduLevelForInfos"

        # 200

        r = s.get(
            route,
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200
        data = r.json()
        assert isinstance(data, list)


def test_get_edu_level_for_infos_id():
    with requests.Session() as s:
        route = "{base}/EduLevelForInfoes/GetEduLevelForInfo/{id}"

        # get all

        r = s.get(
            f"{BASE}/EduLevelForInfoes/GetEduLevelForInfos",
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200
        db_data = r.json()

        # 200

        for edu_id in range(1, len(db_data)):
            r = s.get(
                route.format(base=BASE, id=edu_id),
                headers=HEADERS,
                verify=SSL_VERIFY,
            )

            assert r.status_code == 200
            data = r.json()
            assert data["id"] == edu_id
            assert db_data[edu_id - 1]["name"] == data["name"]
            assert data["lastUpdate"] == "2019-01-01T00:00:00"

        # 404

        r = s.get(
            route.format(base=BASE, id=0),
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 404
