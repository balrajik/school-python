import n1


def test_bubblesort():
    assert n1.bubblesort([6, 4, 1, 3, 2, 7, 5]) == [1, 2, 3, 4, 5, 6, 7]


def test_bubblesort_with_negative_numbers():
    assert n1.bubblesort([-9, 5, 2, -4, 4, -8]) == [-9, -8, -4, 2, 4, 5]


def test_bubblesort_with_fractional_numbers():
    assert n1.bubblesort([2, 7, 1, 0.2, -0.75]) == [-0.75, 0.2, 1, 2, 7]