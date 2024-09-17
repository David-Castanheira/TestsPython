# Função de cálculo de volume
def calcula_volume(comprimento, largura, altura):
    return comprimento * largura * altura

try:
    resultado = calcula_volume(1, 1, 1)
    assert resultado == 1
    print("O volume é igual a 1")

except AssertionError:
    print("O resultado está errado")

try:
    resultado = calcula_volume(2, 4, 3)
    assert resultado == 24
    print("O volume é igual a 24")

except AssertionError:
    print("O resultado está errado")

try:
    resultado = calcula_volume(5, 5, 2)
    assert resultado == 100
    print("O volume é igual a 100")

except AssertionError:
    print("O resultado está errado")