from . import solution


def test_1():
    res = solution([1, 5, 5, 2, 6])

    assert res == 4


def test_2():
    res = solution([1, 1, 1, 1])

    assert res == 4


def test_3():
    res = solution([1, 4, 5, 71])

    assert res == 4


def test_4():
    res = solution([4, 3, 2, 0])

    assert res == 4



def test_5():
    res = solution([0, 10, 4, 1, 11, 0])

    assert res == 4


def test_6():
    res = solution([1, 0, 1])

    assert res == 3



def test_7():
    res = solution([0, 1, 0])

    assert res == 2