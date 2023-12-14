import pytest

from tests.session import Session


@pytest.fixture(scope='session')
def s():
    with Session() as session:
        yield session
