from americana.calculator.add import calculator


def test_calculator():
    assert calculator(5, 6) == 11
    assert calculator(7, 11) == 18
