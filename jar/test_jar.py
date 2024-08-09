from jar import Jar

def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar2 = Jar(3)
    assert jar2.capacity == 3


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(11)
    assert jar.size == 12


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(1)
    assert jar.size == 11
    jar.withdraw(10)
    assert jar.size == 1


if __name__ == "__main__":
    main()




