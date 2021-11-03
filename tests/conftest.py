# PSL
import pytest

# Own
from book_scraper import create_app


@pytest.fixture()
def test_client():
    flask_app = create_app()
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client



