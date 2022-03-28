import calculator

def test_add():
    x = 20
    y = 10
    result=calculator.add(x,y)
    assert result == x+y

def test_sub():
    x = 20
    y = 10
    result=calculator.sub(x,y)
    assert result == x-y

def test_mul():
    x = 20
    y = 10
    result=calculator.mul(x,y)
    assert result == x*y

def test_div():
    x = 20
    y = 10
    result=calculator.div(x,y)
    assert result == x/y