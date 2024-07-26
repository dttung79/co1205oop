from my_function import my_sum

def test_my_sum_01():
    n = 0
    s = 0
    assert s == my_sum(n)

def test_my_sum_02():
    n = 5
    s = 15
    assert s == my_sum(n)

def test_my_sum_03():
    n = -5
    s = -15
    assert s == my_sum(n)