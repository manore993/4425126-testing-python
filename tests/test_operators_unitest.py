import unittest
from calculate.operators import Operators

class TestUtils(unittest.TestCase):
    def test_addition(self):
        sut = Operators()
        operation = "5.5 + 10 + 30 + 13.7"
        expected_value = 59.2
        self.assertEqual(sut.addition(operation), expected_value)

    def test_substraction(self):
        sut = Operators()
        operation = "5.5 - 10 - 30 - 13.7"
        expected_value = -48.2
        self.assertEqual(sut.substraction(operation), expected_value)

    def test_multiplication(self):
        sut = Operators()
        operation = "5.5 * 10 * 30 * 13.7"
        expected_value = 22605
        self.assertEqual(sut.multiplication(operation), expected_value)

    def test_division(self):
        sut = Operators()
        operation = "5.5 / 10"
        expected_value = 0.55
        self.assertEqual(sut.division(operation), expected_value)

if __name__ == '__main__':
    unittest.main()
