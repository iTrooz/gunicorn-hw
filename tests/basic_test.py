from utils import app

def test_http_code(app):
    resp = app.test_client().get("/")
    assert resp.status_code == 200
