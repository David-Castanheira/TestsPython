# Função que gera números de 1 a 100 definido condições como descritas no exercício
def fizzbuzz(n):
    lista = []
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            lista.append('FizzBuzz')
        elif n % 3 == 0:
            lista.append('Fizz')
        elif n % 5 == 0:
            lista.append('Buzz')
        else:
            lista.append(n)
    return lista

# Exibição da lista percorrendo e imprimindo cada item em cada linha 
def exibir_lista(lista):
    for item in lista:
        print(item)

# Chamada da função e impressão na tela 
resultado = fizzbuzz(100)
exibir_lista(resultado)