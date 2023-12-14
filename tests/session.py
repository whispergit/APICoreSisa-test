from typing import Any

from requests import Response, Session as _Session

from tests.constants import BASE, HEADERS, SSL_VERIFY


class Session(_Session):
    def __init__(self) -> None:
        super().__init__()
        self.headers.update(HEADERS)
        self.verify = SSL_VERIFY

    def request(
        self,
        method: str,
        url: str,
        **kwargs: Any,
    ) -> Response:
        if url.startswith('/'):
            url = BASE + url
        return super().request(
            method=method,
            url=url,
            **kwargs,
        )
