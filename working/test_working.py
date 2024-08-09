from working import convert
import pytest

def main():
    test_success()
    test_valueError()

def test_success():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"


def test_valueError():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("13 AM 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")  # Test for missing "to"
    with pytest.raises(ValueError):
        convert("25 AM to 5 PM")  # Test for out-of-range times

if __name__ == "__main__":
    main()
