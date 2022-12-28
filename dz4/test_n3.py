import n3


def test_get_intersection():
    assert n3.get_intersection({1, 3, 5, 7}, {5, 1}) == {1, 5}

def test_get_intersection_with_negative_numbers():
    assert n3.get_intersection({-5, 5, 1, 4, -2}, {5, 1, -2}) == {-2,1,5}

def test_get_intersection_with_fractional_numbers():
    assert n3.get_intersection({0.34, -2.45, 1, -2, 5}, {1, -2.45, 0.34}) == {-2.45, 0.34, 1}


def test_get_difference():
    assert n3.get_difference({1, 3, 5, 7}, {5, 1}) == {3,7}

def test_get_difference_with_negative_numbers():
    assert n3.get_difference({-5, 5, 1, 4, -2}, {5, 1, -2}) == {-5, 4}

def test_get_difference_with_fractional_numbers():
    assert n3.get_difference({0.34, -2.45, 1, -2, 5}, {1, -2.45, 0.34}) == {-2, 5}


def test_get_symmetric_difference(): 
    assert n3.get_symmetric_difference({1, 3, 5, 7}, {5, 1,6}) == {3,7,6}

def test_get_symmetric_difference_with_negative_numbers(): 
    assert n3.get_symmetric_difference({-5, 5, 1, 4, -2}, {5, 1, -2}) == {-5, 4}

def test_get_symmetric_difference_with_fractional_numbers(): 
    assert n3.get_symmetric_difference({0.34, -2.45, 1, -2, 5}, {1, -2.45, 0.34}) == {-2, 5}