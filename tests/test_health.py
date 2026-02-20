from app.main import app


def test_health_v1() -> None:
    client = app.test_client()
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_settings_v1() -> None:
    client = app.test_client()
    response = client.get("/api/v1/settings")
    assert response.status_code == 200
    payload = response.get_json()
    assert payload["service_name"]
    assert payload["environment"]
    assert payload["api_v1_prefix"]
