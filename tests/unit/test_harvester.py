from search import Harvester

PRODUCT = {
    "id": 1,
    "name": "Acai + Cherry",
    "collection": "Smoothie",
    "ingredientIds": [31, 79, 81, 4, 51, 67],
    "image": {
        "url": "http://www.daily-harvest.com/static/img/products/01-acai/product-shot-ingredients.jpeg"
    },
}


def test_search_by_ingredient():
    # apply the monkeypatch for requests.get to mock_get

    results = Harvester().fetch_products_by_ingredient("Organic Banana")

    assert len(results) == 16
    assert isinstance(results, list)
    assert isinstance(results[0], dict)

    assert PRODUCT in results
