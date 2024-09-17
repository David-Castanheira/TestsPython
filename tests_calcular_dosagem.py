import pytest
from controllers.calcular_dosagem import calcular_dosagem

# Testes com pytest
def test_dosagem1():
    assert ValueError, calcular_dosagem(-1, 5)

def test_dosagem2():
    assert ValueError, calcular_dosagem(250, 5)

def test_dosagem3():
    assert calcular_dosagem(20, 60)

def test_dosagem4():
    assert calcular_dosagem(12, 60)

def test_dosagem5():
    assert calcular_dosagem(20, 59)

def test_dosagem6():
    assert calcular_dosagem(12, 59)

def test_dosagem7():
    assert calcular_dosagem(1, 5)

def test_dosagem8():
    assert calcular_dosagem(1, 9)

def test_dosagem9():
    assert calcular_dosagem(2, 9.1)

def test_dosagem10():
    assert calcular_dosagem(2, 16)

def test_dosagem11():
    assert calcular_dosagem(3, 16.1)

def test_dosagem12():
    assert calcular_dosagem(3, 24)

def test_dosagem13():
    assert calcular_dosagem(4, 24.1)

def test_dosagem14():
    assert calcular_dosagem(5, 30)

def test_dosagem15():
    assert calcular_dosagem(6, 30.1)