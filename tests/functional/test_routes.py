from recipesapi import app
import pytest

def test_get_recipe(testing_client):
    response = testing_client.get('/')
    assert response.status_code == 200


def test_dummy_wrong_route(): 

    with app.test_client() as client:
        response = client.get('/wrong_route')
        assert response.status_code == 404
