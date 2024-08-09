from um import count

def main():
    test_with_um()
    test_without_um()
    test_with_insider_um()


def test_with_um():
    assert count("um") == 1
    assert count("Hello, um, how are you") == 1
    assert count("Hello um, um") == 2
    assert count("Hello UM, Um") == 2 

def test_without_um():
    assert count("Greeting") == 0
    assert count("") == 0

def test_with_insider_um():
    assert count("hows it going, its yummy") == 0
    assert count("This drump is yours?") == 0

if __name__ == "__main__":
    main()
