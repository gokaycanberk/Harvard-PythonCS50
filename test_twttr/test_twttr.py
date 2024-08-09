from twttr import shorten

def main():
    test_shorten_upper_lower_casese()
    test_shorten_number()
    test_shorten_punction()


def test_shorten_upper_lower_casese():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("twITTer") == "twTTr"

def test_shorten_number():
    assert shorten("1234") == "1234"

def test_shorten_punction():
    assert shorten(".,!") == ".,!"
