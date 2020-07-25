from cli import main, get_args


def test_main():
    assert main.__name__ == "main"

    # Further testing could be accomplished here by mocking out the Harvester object,
    # either by monkeypatching it or by passing a mock to main


def test_get_args():
    assert get_args.__name__ == "get_args"
