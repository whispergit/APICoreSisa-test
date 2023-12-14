# BASE: str = "https://localhost:7036"
BASE: str = "http://172.20.24.63:80/new"

ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJBbmRyb2lkIiwiZnVsbE5hbWUiOiJBbmRyb2lkIEFQSSBDbGllbnQiLCJyb2xlIjoiQWRtaW4iLCJqdGkiOiIxMmIxOTlkYy03NWFhLTQzYmMtYWE2Zi01MDlkZDBiNjcyNmEiLCJleHAiOjE3MTAxMjMzNDgsImlzcyI6Imh0dHBzOi8vc3RvdS5hYy50aCIsImF1ZCI6Imh0dHBzOi8vc3RvdS5hYy50aCJ9._X72NLRtEyiasUkPvZoy9HxBgk32PS3GkqugoUcVqJ8"

HEADERS = {
    "Authorization": "Bearer %s" % ACCESS_TOKEN,
}

SSL_VERIFY = False
