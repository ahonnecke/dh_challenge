# coding: utf-8

"""Test that imports work"""


def test_import_harvester():
    from search import Harvester

    assert Harvester.__name__ == "Harvester"


def test_import_app():
    import app

    assert app.__name__ == "app"
