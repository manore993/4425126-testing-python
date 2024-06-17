from calculate.operators import Operators

def test_addition():
    sut = Operators()
    operation = "5.5 + 10 + 30 + 13.7"
    expected_value = 59.2
    assert sut.addition(operation) == expected_value

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
