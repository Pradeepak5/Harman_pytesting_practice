import calculator
import pytest

@pytest.mark.parametrize("x,y,z",[(2,3,5),(1,3,4),(1,1,0)])
def test_add(x,y,z):
    result=calculator.add(x,y)
    assert result == z

@pytest.mark.parametrize("x,y,z",[(3,3,0),(3,1,2),(3,2,0)])
def test_sub(x,y,z):
    result=calculator.sub(x,y)
    assert result == z

@pytest.mark.parametrize("x,y,z",[(3,3,9),(1,2,3)])
def test_mul(x,y,z):
    result=calculator.mul(x,y)
    assert result == z

@pytest.mark.parametrize("x,y,z",[(3,3,1),(2,2,2)])
def test_div(x,y,z):
    result=calculator.div(x,y)
    assert result == z