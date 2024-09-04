import unittest
from controllers.media_notas import avaliar_notas

# Testes unitários  
class TestSoma(unittest.TestCase):
    def test_avaliacao_notas1(self):
        self.assertRaises(ValueError, avaliar_notas, -1, 0, 0, 0)

    def test_avaliacao_notas2(self):
        self.assertRaises(ValueError, avaliar_notas, 0, -1, 0, 0)

    def test_avaliacao_notas3(self):
        self.assertRaises(ValueError, avaliar_notas, -0, 0, -1, 0)

    def test_avaliacao_notas4(self):
        self.assertEqual(avaliar_notas(10, 10, 10, 10), 'A')

    def test_avaliacao_notas5(self):
        self.assertEqual(avaliar_notas(9, 9, 9, 9), 'A')

    def test_avaliacao_notas6(self):
        self.assertEqual(avaliar_notas(8.9, 8.9, 8.9, 8.9), 'B')

    def test_avaliacao_notas7(self):
        self.assertEqual(avaliar_notas(7.5, 7.5, 7.5, 7.5), 'B')

    def test_avaliacao_notas8(self):
        self.assertEqual(avaliar_notas(7.4, 7.4, 7.4, 7.4), 'C')

    def test_avaliacao_notas9(self):
        self.assertEqual(avaliar_notas(6.0, 6.0, 6.0, 6.0), 'C')

    def test_avaliacao_notas10(self):
        self.assertEqual(avaliar_notas(5.9, 5.9, 5.9, 5.9), 'D')

    def test_avaliacao_notas11(self):
        self.assertEqual(avaliar_notas(0.0, 0.0, 0.0, 0.0), 'D')    

if __name__ == '__main__':
    unittest.main()