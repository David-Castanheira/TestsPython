def soma(a, b):
    return a + b

# Programa principal
# Test Case 01
try:
    resultado = soma(10, 20)
    assert resultado == 30
    print("Soma correta")

except AssertionError:
    print("Soma incorreta")

# Test Case 02
try:
    resultado = soma(3, 5)
    assert resultado == 8
    print("Soma correta")

except AssertionError:
    print("Soma incorreta")

# Test Case 03
try:
    resultado = soma(10, 12)
    assert resultado == 22
    print("Soma correta")

except AssertionError:
    print("Soma incorreta")