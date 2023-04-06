from main import recursive_summ


def test_recursive_summ():
    assert 45 == recursive_summ([1, 2, 3, 4, 5, 6, 7, 8, 9])
