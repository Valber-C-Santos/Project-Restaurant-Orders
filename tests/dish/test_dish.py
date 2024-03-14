import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient

def test_dish():

    dish = Dish("Lasanha", 25.0)
    assert dish.name == "Lasanha"

    dish1 = Dish("Pizza", 30.0)
    dish2 = Dish("Pizza", 30.0)
    assert hash(dish1) == hash(dish2)

    dish3 = Dish("Hambúrguer", 20.0)
    assert hash(dish1) != hash(dish3)

    assert dish1 == dish2

    assert dish1 != dish3

    assert repr(dish1) == "Dish('Pizza', R$30.00)"

    with pytest.raises(TypeError):
        Dish("Lasanha", "25.0")

    with pytest.raises(ValueError):
        Dish("Lasanha", -25.0)

    dish.add_ingredient_dependency(Ingredient("Carne"), 200)
    assert dish.recipe.get(Ingredient("Carne")) == 200

    assert dish.get_restrictions() == set()

    assert dish.get_ingredients() == {Ingredient("Carne")}

if __name__ == "__main__":
    pytest.main()
