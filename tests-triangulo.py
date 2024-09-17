import pytest 
from controllers.triangulo import triangulo

def test_triangulo_TypeError_a():
    with pytest.raises(TypeError):
        triangulo('2', 5, 4)

def test_triangulo_TypeError_b():
    with pytest.raises(TypeError):
        triangulo(2, '5', 4)

def test_triangulo_TypeError_c():
    with pytest.raises(TypeError):
        triangulo(2, 5, '4')

def test_triangulo_escaleno():
    assert triangulo(2, 5, 4) == 'Triângulo escaleno'

def test_triangulo_isoceles():
    assert triangulo(4, 5, 4) == 'Triângulo isóceles'

def test_triangulo_equilatero():
    assert triangulo(4, 4, 4) == 'Triângulo equilátero'

def test_triangulo_nao_triangulo():
    assert triangulo(0, 4, 4) == 'Não é um triângulo'