# Função que recebe três parâmetros: a, b e c. Esses parâmetros representam os três lados de um triângulo.
def triangulo(a, b, c):
    # Verifica se o valor a não é do tipo booleano e inteiro e retorna um typerror
    if type(a) != float and type(a) != int:
        raise TypeError()
    # Verifica se o valor b não é do tipo booleano e inteiro e retorna um typerror
    if type(b) != float and type(b) != int:
        raise TypeError()
    # Verifica se o valor c não é do tipo booleano e inteiro e retorna um typerror    
    if type(c) != float and type(c) != int:
        raise TypeError()
    
    # Após verificar os tipos de dados, a função verifica se o triângulo é válido usando a regra da somatória
    # Isso garante que a soma de qualquer duas laterais seja maior que a terceira lateral, o que é necessário para formar um triângulo.
    if a + b > c and a + c > b and b + c > a:
        # Se todos os lados tiverem a mesma medida
        if a == b and b == c:
            return 'Triângulo equilátero'
        # Se dois lados tiverem a mesma medida
        elif a == b or a == c or b == c:
            return 'Triângulo isóceles'
        # Lados com valores distintos 
        else:
            return 'Triângulo escaleno'
    else:
        return 'Não é um triângulo'