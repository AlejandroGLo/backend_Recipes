
from recipesapi.models import Recipe
import pytest

def test_create_recipe(): 
    recipe = Recipe(name='test', ingredients='test', instructions='test', favorite=False, rating=0)
    assert recipe.name == 'test'
    assert recipe.ingredients == 'test'
    assert recipe.instructions == 'test'
    assert recipe.favorite == False
    assert recipe.rating == 0


