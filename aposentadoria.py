import unittest

REQUERER = 'Requerer aposentadoria'
NAO_REQUERER = 'Não requerer aposentadoria'

def verificar_qualificacao_empregado(idade: int, tempo_de_servico: int):

    # Verifica se idade é igual a 0
    # Em caso afirmativo, retorna um erro
    if idade == 0:
        raise ValueError('Idade igual a 0')

    # Verifica se o tempo de serviço é igual a 0
    # Em caso afirmativo, retorna um erro
    if tempo_de_servico == 0:
        raise ValueError('Tempo de serviço iguais a 0')

    # Verifica se o tipo da variável idade não é um inteiro
    # Em caso afirmativo, retorna um erro
    if type(idade) != int:
        raise TypeError(f'Tipo 1 incompatível')

    # Verifica se o tipo da variável tempo_de_servico não é um inteiro
    # Em caso afirmativo, retorna um erro
    if type(tempo_de_servico) != int:
        raise TypeError(f'Tipo 2 incompatível')
    
    if idade >= 65:
        return REQUERER
    elif tempo_de_servico >= 30:
        return REQUERER
    elif idade >= 60 and tempo_de_servico >= 25:
        return REQUERER

    return NAO_REQUERER

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