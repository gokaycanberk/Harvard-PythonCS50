from bank import value

def main():
    test_greeting_zero()
    test_greeting_hundered()
    test_greeting_twenty()


def test_greeting_zero():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("Hello HEY") == 0


def test_greeting_hundered():
    assert value("Greeting") == 100
    assert value("greeting") == 100

def test_greeting_twenty():
    assert value("hows it going") == 20
    assert value("Hows it going") == 20

