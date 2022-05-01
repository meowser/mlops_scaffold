from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API.  Call /search or /wiki"}


def test_read_phrase():
    response = client.get("/phrase/Terrence Gilliam")
    assert response.status_code == 200
    assert response.json() == {
        "result": [
            "terrence vance gilliam",
            "november",
            "american-born",
            "british film director",
            "monty python",
            "comedy troupe",
        ]
    }
