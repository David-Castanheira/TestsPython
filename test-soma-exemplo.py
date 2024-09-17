import unittest

# Função de soma simples entre dois valores
def soma(a, b):
    return a + b

class TesteSoma(unittest.TestCase):
    def test_funcao_soma(self):
        self.assertEqual(soma(10, 10), 20)

if __name__ == '__main__':
    unittest.main()