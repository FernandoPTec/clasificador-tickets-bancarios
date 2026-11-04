import os
import sys

sys.path.append(os.path.abspath("."))

from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert "mensaje" in response.json()
