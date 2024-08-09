from seasons import check_birthdate

def main():
    test_true_date_format()
    test_wrong_date_format()

def test_true_date_format():
    assert check_birthdate("1988-06-04") == ("1988", "06", "04")

def test_wrong_date_format():
    assert check_birthdate("19880604") == None
    assert check_birthdate("1988 june 04") == None


if __name__ == "__main__":
    main()
