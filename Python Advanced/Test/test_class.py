class Calculator:

    def add(
        self,
        a,
        b
    ):
        return a + b


def test_calculator():

    calc = Calculator()

    assert calc.add(
        5,
        5
    ) == 10
