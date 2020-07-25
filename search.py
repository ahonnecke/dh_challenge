import json


class Harvester:
    _ingredients: dict = {}

    @property
    def ingredients(self):
        if not self._ingredients:
            # @TODO get these into a database, index by name
            with open("fixtures/ingredients.json") as json_file:
                for x in json.load(json_file):
                    self._ingredients[x.get("name")] = x

        return self._ingredients

    @property
    def products(self):
        # @TODO get these into a database, n2m FK to ingredients
        with open("fixtures/products.json") as json_file:
            return json.load(json_file)

    def fetch_products_by_ingredient(self, ingredient: str):
        ingredient_id = self.ingredients.get(ingredient, {}).get("id")

        if not ingredient_id:
            return None

        out = []
        for product in self.products:
            if ingredient_id in product["ingredientIds"]:
                out.append(product)

        return out
