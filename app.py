from flask import Flask, request, jsonify
from search import Harvester

app = Flask(__name__)


@app.route("/healthcheck/")
def healthcheck():
    return "OK"


@app.route("/")
def search():
    ingredient = request.args.get("ingredient")
    return jsonify(Harvester().fetch_products_by_ingredient(ingredient))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
