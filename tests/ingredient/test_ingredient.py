from src.models.ingredient import Ingredient, Restriction # noqa: F401, E261, E501


def test_ingredient():
    ingredient = Ingredient("Tomato")
    assert ingredient.name == "Tomato"
    assert ingredient.restrictions == set()

    ingredient = Ingredient("Milk")
    ingredient.restrictions.add(Restriction.LACTOSE)
    ingredient.restrictions.add(Restriction.GLUTEN)
    assert ingredient.restrictions == {Restriction.LACTOSE, Restriction.GLUTEN}

    ingredient = Ingredient("Onion")
    assert repr(ingredient) == "Ingredient('Onion')"

    ingredient1 = Ingredient("Salt")
    ingredient2 = Ingredient("Salt")
    ingredient3 = Ingredient("Sugar")
    assert ingredient1 == ingredient2
    assert ingredient1 != ingredient3

    hash_equal_for_equal_objects = hash(ingredient1) == hash(ingredient2)
    assert hash_equal_for_equal_objects, "Hashes should be equal for equal objects"

    hash_different_for_different_objects = hash(ingredient1) != hash(ingredient3)
    assert hash_different_for_different_objects, "Hashes should be different for different objects"

    ingredient = Ingredient("Potato")
    assert ingredient.name == "Potato"

    ingredient = Ingredient("Egg")
    ingredient.restrictions.add(Restriction.ANIMAL_DERIVED)
    assert ingredient.restrictions == {Restriction.ANIMAL_DERIVED}
