from app.main import app


def test_health_endpoint():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_accounts_endpoint():
    client = app.test_client()

    response = client.get("/accounts")

    assert response.status_code == 200
    assert len(response.json["accounts"]) == 2