import unittest
from numb3rs import validate


class TestValidate(unittest.TestCase):
    def test_valid_ip(self):
        self.assertTrue(validate("192.168.0.1"))
        self.assertTrue(validate("255.255.255.255"))

    def test_invalid_ip(self):
        self.assertFalse(validate("256.0.0.0"))
        self.assertFalse(validate("192.168.0.256"))

if __name__ == "__main__":
    unittest.main()
