from . import solution


def test_1():
    res = solution("ab?ac?")

    assert res == "abcacd"



def test_2():
    res = solution("rd?e?wg??")

    assert res == "rdfefwghi"