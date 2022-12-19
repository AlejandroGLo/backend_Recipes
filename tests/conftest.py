import pytest
from recipesapi.models import Recipe
from recipesapi import db, app


@pytest.fixture

def testing_client(scope='module'):
    db.create_all()
    recipe = Recipe(name='test', ingredients='test', instructions='test', favorite=False, rating=0)
    db.session.add(recipe)
    db.session.commit()
    
    with app.test_client() as testing_client:
        yield testing_client
    db.drop_all()
