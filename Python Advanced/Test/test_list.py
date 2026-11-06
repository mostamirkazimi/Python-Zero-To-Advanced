def get_count(items):

    return len(items)


def test_get_count():

    assert get_count(
        [1, 2, 3]
    ) == 3