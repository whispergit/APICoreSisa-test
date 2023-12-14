import requests

from tests.constants import BASE, HEADERS, SSL_VERIFY

# GET /QuestioniarDetails/GetQuestioniarDetails
# GET /QuestioniarDetails/GetQuestioniarDetail/{id}
# POST /QuestioniarDetails/PostQuestioniarDetail
# GET /QuestioniarDetails/GetQuestioniarStuDetail/{id}
# GET /QuestioniarDetails/GetCountDetail/{id}

# payload = {
#   "questDId": 0,
#   "questDQuestId": 0,
#   "questDStuId": 0,
#   "questDDate": "2023-12-12T12:34:55.010Z"
# }


def test_get_questioniar_details():
    with requests.Session() as s:
        route = f"{BASE}/QuestioniarDetails/GetQuestioniarDetails"

        # 200

        r = s.get(
            route,
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200

        data = r.json()
        for i in data:
            assert 'questDId' in i
            assert 'questDQuestId' in i
            assert 'questDStuId' in i
            assert 'questDDate' in i


def test_get_questioniar_detail_id():
    with requests.Session() as s:
        route = "{base}/QuestioniarDetails/GetQuestioniarDetail/{id}"

        # get all

        r = s.get(
            f"{BASE}/QuestioniarDetails/GetQuestioniarDetails",
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200
        db_data = r.json()

        # 200

        for questDId in range(1, 5):
            r = s.get(
                route.format(base=BASE, id=questDId),
                headers=HEADERS,
                verify=SSL_VERIFY,
            )

            assert r.status_code == 200
            data = r.json()
            for i in data:
                for db in db_data:
                    if db["questDId"] == questDId:
                        assert db["questDQuestId"] == data["questDQuestId"]
                        assert db["questDStuId"] == data["questDStuId"]
                        assert db["questDDate"] == data["questDDate"]

        # 404

        r = s.get(
            route.format(base=BASE, id=0),
            headers=HEADERS,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 404


def test_post_questioniar_detail():
    with requests.Session() as s:
        route = f"{BASE}/QuestioniarDetails/PostQuestioniarDetail"

        # 200

        payload = {
            # "questDId": 0, # auto increment
            "questDQuestId": 1,
            "questDStuId": 105,
            # "questDDate": "2023-12-12T12:34:55.010Z",  # auto timestamp
        }

        r = s.post(
            route,
            headers=HEADERS,
            json=payload,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 200

        # data = r.json()
        # assert data["questDId"] == 5
        # assert data["questDQuestId"] == 0
        # assert data["questDStuId"] == 0
        # assert data["questDDate"] == "2023-12-12T12:34:55.010Z"

        # 404

        payload = {
            # "questDId": 0, # auto increment
            "questDQuestId": 0,
            "questDStuId": 0,
            # "questDDate": "2023-12-12T12:34:55.010Z",  # auto timestamp
        }

        r = s.post(
            route,
            headers=HEADERS,
            json=payload,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 404

        # 404

        payload = {
            # "questDId": 0, # auto increment
            # "questDQuestId": 0,
            # "questDStuId": 0,
            # "questDDate": "2023-12-12T12:34:55.010Z",  # auto timestamp
        }

        r = s.post(
            route,
            headers=HEADERS,
            json=payload,
            verify=SSL_VERIFY,
        )

        assert r.status_code == 404


def test_get_questioniar_stu_detail_id():
    with requests.Session() as s:
        route = "{base}/QuestioniarDetails/GetQuestioniarStuDetail/{id}"

        # get all

        db_data = [
            {
                "stuCode": "5670010718",
                "stuName": "นายทดสอบ  19:26",
                "stuDegree": "ปริญญาตรี",
                "questDDate": None,
            },
            {
                "stuCode": "6196013178",
                "stuName": "นายทดสอบ  16:11",
                "stuDegree": "ปริญญาตรี",
                "questDDate": "2023-12-08T11:48:25.417",
            },
        ]

        # 200

        with requests.Session() as s:
            route = "{base}/QuestioniarDetails/GetQuestioniarStuDetail/{id}"

            r = s.get(
                route.format(base=BASE, id=1),
                headers=HEADERS,
                verify=SSL_VERIFY,
            )

            assert r.status_code == 200
            data = r.json()
            assert data == db_data

            r = s.get(
                route.format(base=BASE, id=0),
                headers=HEADERS,
                verify=SSL_VERIFY,
            )

            assert r.status_code == 200

            data = r.json()
            assert data == []


def test_get_count_detail_id():
    with requests.Session() as s:
        route = "{base}/QuestioniarDetails/GetCountDetail/{id}"

        with requests.Session() as s:
            route = "{base}/QuestioniarDetails/GetCountDetail/{id}"

            # 200

            r = s.get(
                route.format(base=BASE, id=1),
                headers=HEADERS,
                verify=SSL_VERIFY,
            )

            assert r.status_code == 200
            data = r.json()
            assert data == 2

            r = s.get(
                route.format(base=BASE, id=0),
                headers=HEADERS,
                verify=SSL_VERIFY,
            )

            assert r.status_code == 200

            data = r.json()
            assert data == 0
