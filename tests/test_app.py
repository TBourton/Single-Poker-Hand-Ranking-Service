from typing import Generator

import fastapi
import pytest
from fastapi.testclient import TestClient

from app import app as _app


@pytest.fixture
def app() -> Generator[fastapi.FastAPI, None, None]:
    yield _app


@pytest.fixture
def client(app: fastapi.FastAPI) -> Generator[TestClient, None, None]:
    with TestClient(app) as client_:
        yield client_


def test_health(client: TestClient):
    assert client.get("/docs").status_code == 200
