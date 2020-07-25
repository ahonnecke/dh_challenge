# Local Installation
## Install docker
 * https://docs.docker.com/get-docker/
## Install docker compose
 * https://docs.docker.com/compose/install/
##

# Linting Locally
`docker-compose run lint`

# Running Unit Tests Locally
`docker-compose run unit-tests`

``` bash
======================= test session starts ========================
platform linux -- Python 3.7.7, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
rootdir: /app, inifile: setup.cfg, testpaths: ./tests/unit
plugins: cov-2.10.0
collected 3 items

tests/unit/test_harvester.py .                                                                                                                                                         [ 33%]
tests/unit/test_import.py ..                                                                                                                                                           [100%]

======================== 3 passed in 0.04s =========================
======================= test session starts ========================
platform linux -- Python 3.7.7, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
rootdir: /app, inifile: setup.cfg, testpaths: ./tests/unit
plugins: cov-2.10.0
collected 3 items

tests/unit/test_harvester.py .                                                                                                                                                         [ 33%]
tests/unit/test_import.py ..                                                                                                                                                           [100%]

------ generated xml file: /tmp/test_results/pytest/results.xml ------

----------- coverage: platform linux, python 3.7.7-final-0 -----------
Name                           Stmts   Miss  Cover
--------------------------------------------------
app.py                            13      6    54%
search.py                         21      1    95%
tests/unit/test_harvester.py       6      0   100%
tests/unit/test_import.py          7      0   100%
--------------------------------------------------
TOTAL                             47      7    85%

Required test coverage of 80% reached. Total coverage: 85.11%
======================== 3 passed in 0.09s =========================
ahonnecke@homonym:~/Documents/professional/challenges/daily_harvest$
```

# CLI Usage

## Help Menu
`$ docker-compose run cli --help`

``` bash
usage: cli.py [-h] ingredient

Print location and time of the ISS

positional arguments:
  ingredient  Specify the ingredient to search for

optional arguments:
  -h, --help  show this help message and exit
```

## Example Usage
`docker-compose run app app "Pine Pollen"`

``` bash
[{"id": 68, "name": "Black Sesame + Banana", "collection": "Smoothie", "ingredientIds": [79, 81, 17, 214, 42, 215], "image": {"url": "http://www.daily-harvest.com/static/img/products/a23-sesa/product-shot-ingredients.jpeg"}}]
```

## Local API
`docker-compose up`

`wget http://127.0.0.1:5000/?ingredient=Organic+Banana`

``` bash
ahonnecke@homonym:~/Documents/professional/challenges$ head index.html\?ingredient\=Organic+Banana
[
  {
    "collection": "Smoothie",
    "id": 1,
    "image": {
      "url": "http://www.daily-harvest.com/static/img/products/01-acai/product-shot-ingredients.jpeg"
    },
    "ingredientIds": [
      31,
      79,
```

![image](https://user-images.githubusercontent.com/419355/88466565-f043b800-ce8a-11ea-81ab-ddd268bfb927.png)
