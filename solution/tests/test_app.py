from typing import Generator

import pytest

import fastapi
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


def test_rank_happy(client: TestClient):
    hand = "2H 3D 5S 9C KD"
    resp = client.post("/rank", json={"hand": hand})
    assert resp.status_code == 200

    assert resp.text == "high card: King"


@pytest.mark.parametrize("hand", ["foo", "22H 333333D 5S 9C KD"])
def test_rank_unhappy(client: TestClient, hand: str):
    resp = client.post("/rank", json={"hand": hand})
    assert resp.status_code == 500
