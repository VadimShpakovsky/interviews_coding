from . import solution


def test_0():
    res = solution([1, 1, 2])

    assert res == 2

def test_1():
    res = solution([51, 71, 17, 42])

    assert res == 93


def test_2():
    res = solution([42, 33, 60])

    assert res == 102


def test_3():
    res = solution([51, 32, 43])

    assert res == -1