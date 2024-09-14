import pytest
from controllers.peso import obter_peso

def test_peso1():
    assert obter_peso(1.5, 'M') == pytest.approx(51.05, 0.01)

def test_peso2():
    assert obter_peso(1.5, 'F') == pytest.approx(48.45, 0.01)

def test_peso3():
    assert obter_peso(1.6, 'M') == pytest.approx(58.32, 0.01)

def test_peso4():
    assert obter_peso(1.6, 'F') == pytest.approx(54.66, 0.01)

def test_peso5():
    assert obter_peso(1.7, 'M') == pytest.approx(65.59, 0.01)

def test_peso6():
    assert obter_peso(1.7, 'F') == pytest.approx(60.86, 0.01)

def test_peso7():
    assert obter_peso(1.8, 'M') == pytest.approx(72.86, 0.01)

def test_peso8():
    assert obter_peso(1.8, 'F') == pytest.approx(67.08, 0.01)

def test_peso9():
    assert obter_peso(1.9, 'M') == pytest.approx(80.13, 0.01)

def test_peso10():
    assert obter_peso(1.9, 'F') == pytest.approx(73.28, 0.01)

def test_peso11():
    assert obter_peso(2.0, 'M') == pytest.approx(87.4, 0.01)
    
def test_peso12():
    assert obter_peso(2.0, 'F') == pytest.approx(79.5, 0.01)