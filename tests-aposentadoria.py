import unittest
from controllers.aposentadoria import verificar_qualificacao_empregado, REQUERER, NAO_REQUERER

# Testes unitários
class TestEmpregado(unittest.TestCase):
    def test_qualificacao1(self):
        self.assertEqual(verificar_qualificacao_empregado(65, 20), REQUERER)

    def test_qualificacao2(self):
        self.assertEqual(verificar_qualificacao_empregado(59, 30), REQUERER)

    def test_qualificacao3(self):
        self.assertEqual(verificar_qualificacao_empregado(60, 25), REQUERER)

    def test_qualificacao4(self):
        self.assertEqual(verificar_qualificacao_empregado(59, 24), NAO_REQUERER)

    def test_qualificacao5(self):
        self.assertRaises(ValueError, verificar_qualificacao_empregado, 0, 10)

    def test_qualificacao6(self):
        self.assertRaises(ValueError, verificar_qualificacao_empregado, 20, 0)

    def test_qualificacao7(self):
        self.assertRaises(TypeError, verificar_qualificacao_empregado, '65', 30)

    def test_qualificacao8(self):
        self.assertRaises(TypeError, verificar_qualificacao_empregado, 65, '30')

if __name__ == '__main__':
    unittest.main()