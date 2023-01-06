import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestEndpoints:
    """
    Test all api endpoint connections.

    TODO: more test on function.
    """

    def test_index(self, client):
        """
        Test index page up.
        """
        response = client.get(reverse("index"))
        assert response.status_code == 200

    def test_api_submit_post(self, client):
        """
        Test api endpoint is up.
        """
        response = client.post(reverse("submit"))
        assert response.status_code == 200

    def test_api_submit_get(self, client):
        """
        Test api endpoint does not allow get.
        """
        response = client.get(reverse("submit"))
        assert response.status_code == 405
