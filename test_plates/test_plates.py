from plates import is_valid

def main():
    test_only_numbers()
    test_only_letters()
    test_first_number_zero()
    test_first_number_not_zero()
    test_over_six_characters()
    test_when_numbers_middle()
    test_alphanumeric_characters()


def test_only_numbers():
    assert is_valid("50") == False
    assert is_valid("1234567") == False

def test_only_letters():
    assert is_valid("AB") == True
    assert is_valid("ABCD") == True

def test_first_number_zero():
    assert is_valid("AB01") == False
    assert is_valid("ABA0") == False

def test_first_number_not_zero():
    assert is_valid("AB13") == True
    assert is_valid("AB123") == True

def test_over_six_characters():
    assert is_valid("ABCDEF5") == False
    assert is_valid("AB12345") == False

def test_when_numbers_middle():
    assert is_valid("AB123C") == False
    assert is_valid("AB1234C") == False

def test_alphanumeric_characters():
    assert is_valid("AB@") == False
    assert is_valid("AB#CD") == False
    assert is_valid("AB 123") == False
    assert is_valid("AB.CD") == False
