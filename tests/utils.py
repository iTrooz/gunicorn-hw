import pytest

from exampleapp.main import create_app

@pytest.fixture()
def app():
    app = create_app()
    yield app
    app.stop()
