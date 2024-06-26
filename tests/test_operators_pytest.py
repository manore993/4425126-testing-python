from calculate.operators import Operators
import pytest

@pytest.mark.parametrize("addition, expected_result", [
("3+5", 8),
("5+9", 14),
("8+2", 10),
("4+98", 102),
("90", 90),
("1+2+3+4+5", 15)
])

def test_addition(addition, expected_result):
    sut = Operators()
    # operation = "5.5 + 10 + 30 + 13.7"
    # expected_value = 59.2
    # assert sut.addition(operation) == expected_value
    assert sut.addition(addition) == expected_result

def test_substraction():
    sut = Operators()
    operation = "5.5 - 10 - 30 - 13.7"
    expected_value = -48.2
    assert sut.substraction(operation) == expected_value

def test_multiplication():
    sut = Operators()
    operation = "5.5 * 10 * 30 * 13.7"
    expected_value = 22605
    assert sut.multiplication(operation) == expected_value

def test_division():
    sut = Operators()
    operation = "5.5 / 10"
    expected_value = 0.55
    assert sut.division(operation) == expected_value
            