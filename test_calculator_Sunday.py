import pytest
import yaml

from pythoncode.calculator import Calculator


def get_data():
    with open('files/data.yml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        paras = datas['data']
        ids = datas['id']
        return [paras, ids]


class TestCalc(Calculator):

    @pytest.mark.parametrize('a,b,expect',
                             get_data()[0],
                             ids=get_data()[1])
    def test_add(self, a, b, expect):
        assert expect == Calculator.add(a, b)

    @pytest.mark.parametrize('a,b,expect',
                             get_data()[0],
                             ids=get_data()[1])
    def test_minus(self, a, b, expect):
        assert expect == Calculator.minus(a, b)

    @pytest.mark.parametrize('a,b,expect',
                             get_data()[0],
                             ids=get_data()[1])
    def test_mul(self, a, b, expect):
        assert expect == Calculator.mul(a, b)

    @pytest.mark.parametrize('a,b,expect',
                             get_data()[0],
                             ids=get_data()[1])
    def test_div(self, a, b, expect):
        assert expect == Calculator.div(a, b)
