import pytest
from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expect", [
        (3, 5, 8), (-1, -2, -3), (0, 0, 0), (-5, 3, -2)
    ], ids=["int", "minus", "zero", "minus+int"])
    def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (3, 5, -2), (5, 2, 3), (0, 0, 0), (-2, -8, 6)
    ], ids=["small-big", "big-small", "zero", "minus"])
    def test_sub(self, a, b, expect):
        assert expect == self.calc.sub(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (3, 5, 15), (-2, -2, 4), (-3, 3, -9), (0, 7, 0)
    ], ids=["int", "minus", "minus*int", "zero"])
    def test_mul(self, a, b, expect):
        assert expect == self.calc.mul(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (10, 5, 2), (-10, -5, 2), (10, -5, -2), (-10, 5, -2), (0, 3, 0)
    ], ids=["int", "minus", "int/minus", "minus/int", "zero"])
    def test_div(self, a, b, expect):
        assert expect == self.calc.div(a, b)
