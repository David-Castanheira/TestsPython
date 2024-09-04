# Função de soma de dois valores
def soma(a, b):
    return a + b

# Test Case 01 com estrutura de exceção 
try:
    resultado = soma(10, 20)
    assert resultado == 30
    print("Soma correta")

except AssertionError:
    print("Soma incorreta")

# Test Case 02 com estrutura de exceção
try:
    resultado = soma(3, 5)
    assert resultado == 8
    print("Soma correta")

except AssertionError:
    print("Soma incorreta")

# Test Case 03 com estrutura de exceção
try:
    resultado = soma(10, 12)
    assert resultado == 22
    print("Soma correta")

except AssertionError:
    print("Soma incorreta")