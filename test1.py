import pytest
from pythoncode.calculator import Calculator


@pytest.mark.parametrize('a,b,expect',
                         [(1, 0, 1)])
def test_1(a, b, expect):
    calc = Calculator()
    assert expect == calc.div(a, b)


def test_b():
    assert 1 == 2
