import unittest 

def soma(a, b):
    if type(a) == int and type(b) == int:
        return a + b
    else:
        raise TypeError(f'Tipo incompatível')

# Testes unitários
class TestSoma(unittest.TestCase):
    def test_funcao_soma(self):
        self.assertEqual(soma(10, 10), 20)

    def test_funcao_tipo_imcompativel(self):
        self.assertRaises(TypeError, soma, 10, '5')

    def test_funcao_tipo_float(self):
        self.assertRaises(TypeError, soma, 100.5, 10.2)

    def test_funcao_tipo_boolean(self):
        self.assertRaises(TypeError, soma, True, False)