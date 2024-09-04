def converte_celsius(fahrenheint):
    celsius = (5.0/9.0) * (fahrenheint - 32)
    return celsius 

def converte_fahrenheint(celsius):
    fahrenheint = 1.8 * celsius + 32
    return fahrenheint

# Testes com estrutura de exceção para Celsius
try:
    temperatura = converte_celsius(32)
    assert temperatura == 0
    print(f"Resultado correto. A temperatura é {temperatura}")

except AssertionError:
    print(f"Resultado incorreto. A temperatura é {temperatura}") 

try:
    temperatura = converte_celsius(27)
    assert temperatura == 80.6
    print(f"Resultado correto. A temperatura é {temperatura}")

except AssertionError:
    print(f"Resultado incorreto. A temperatura é {temperatura}") 

# Testes com estrutura de exceção para Fahrenheint
try:
    temperatura = converte_fahrenheint(0)
    assert temperatura == 32
    print(f"Resultado correto. A temperatura é {temperatura}")

except AssertionError:
    print(f"Resultado incorreto. A temperatura é {temperatura}") 

try:
    temperatura = converte_fahrenheint(41)
    assert temperatura == 5
    print(f"Resultado correto. A temperatura é {temperatura}")

except AssertionError:
    print(f"Resultado incorreto. A temperatura é {temperatura}") 