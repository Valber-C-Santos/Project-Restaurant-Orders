import csv
from src.models.dish import Dish, Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set(self.read_all_dishes(source_path).values())


    def read_all_dishes(self, source_path: str):
        all_dishes = dict()

        with open(source_path, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                dish = row["dish"]
                price_dish = float(row["price"])
                ingredients = row["ingredient"]
                quantity = int(row["recipe_amount"])
                if dish not in all_dishes:
                    all_dishes[dish] = Dish(dish, price_dish)
                all_dishes[dish].add_ingredient_dependency(Ingredient(ingredients), quantity)

        return all_dishes
