import n1


def test_with_normal_password():
    assert n1.check_password('563fhgh12') == True

def test_with_4_symbols():
    assert n1.check_password('123h') == False

def test_with_only_numbers():
    assert n1.check_password('1234567') == False

def test_with_only_chars():
    assert n1.check_password('asdasdasd') == False

def test_with_bad_word():
    assert n1.check_password('mypassword') == False

def test_with_empty():
    assert n1.check_password('') == False