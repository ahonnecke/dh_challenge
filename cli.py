import argparse
import json
from pprint import pprint
from search import Harvester


def get_args():
    parser = argparse.ArgumentParser(description="Print location and time of the ISS")
    parser.add_argument(
        "ingredient", help="Specify the ingredient to search for",
    )
    return parser.parse_args()


def main(args, harvester):
    pprint(json.dumps(harvester.fetch_products_by_ingredient(args.ingredient)))


if __name__ == "__main__":
    args = get_args()
    main(args, Harvester())
