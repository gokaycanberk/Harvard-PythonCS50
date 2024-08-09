from fuel import convert, gauge
import pytest

def main():
    test_failed()
    test_success()
    test_zeroDivisionError()
    test_valueError()
 
def test_success():
    assert convert("1/2") == 50 and gauge(50) == "50%"
    assert convert("1/4") == 25 and gauge(25) == "25%"
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("99/100") == 99 and gauge(99) == "F"

def test_failed():
    assert convert("1/2") != 25 and gauge(50) != "25%"
    assert convert("1/4") != 50 and gauge(25) != "50%"
    assert convert("1/100") != 99 and gauge(1) != "F"
    assert convert("99/100") != 1 and gauge(99) != "E"

def test_zeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_valueError():
    with pytest.raises(ValueError):
        convert("1/")
if __name__ == "__main__":
    main()
