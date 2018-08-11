import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app('default')
    client = app.test_client()
    return client


def test_login_status_code(client):
    assert client.post('/').status_code == 200
