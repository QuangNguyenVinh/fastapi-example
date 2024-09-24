import json
import os

import pytest
from fastapi.testclient import TestClient
from app.core.container import Container
from app.main import App

os.environ["ENV"] = "test"

if os.getenv("ENV") not in ["test"]:
    msg = f"ENV is not test, it is {os.getenv('ENV')}"
    pytest.exit(msg)


def insert_default_data(conn):
    request_default_file = open("./tests/test_data/request.json", "r")
    request_default_data = json.load(request_default_file)


@pytest.fixture
def client():
    app_creator = App()
    app = app_creator.app
    with TestClient(app) as client:
        yield client


@pytest.fixture
def container():
    return Container()
