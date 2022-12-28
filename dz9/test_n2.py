import n2


def test_summ():
    assert n2.summ(1, 2, 3, 4) == 10

def test_summ_with_negative_numbers():
    assert n2.summ(-2, -1, 3, 5) == 5

def test_summ_with_fractional_numbers():
    assert n2.summ(0.45, -0.34, 1) == 1.11