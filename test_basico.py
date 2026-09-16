def sumar(a, b):
    return a + b
 
def test_sumar():
    assert sumar(2, 3) == 5
 
def test_sumar_negativos():
    assert sumar(-1, -1) == -2