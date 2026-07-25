from app import app

def test_home():
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == 200
    assert "Mariama ALIO" in resp.get_json()["etudiant"]

def test_health():
    client = app.test_client()
    resp = client.get('/health')
    assert resp.status_code == 200
