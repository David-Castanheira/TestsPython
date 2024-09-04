# Função de cálculo de notas 
def avaliar_notas(n1, n2, n3, media_exercicios):

    if n1 < 0 or n1 > 10:
        raise ValueError('Valor inválido para n1')

    if n2 < 0 or n2 > 10:
        raise ValueError('Valor inválido para n2')

    if n3 < 0 or n3 > 10:
        raise ValueError('Valor inválido para n3')

    if media_exercicios < 0 or media_exercicios > 10:
        raise ValueError('Valor inválido para media_exercicios')

    # Define o cálculo de aproveitamento da média
    media_aproveitamento = (n1 + 2 * n2 + 3 * n3 + media_exercicios) / 7

    # Verifica se a média é maior ou igual a 9.0, se sim retorna 'A'
    if media_aproveitamento >= 9.0:
        return 'A'

    # Verifica se a média é maior ou igual a 7.5 e menor que 9, se sim retorna 'B'
    elif media_aproveitamento >= 7.5 and media_aproveitamento < 9:
        return 'B'

    # Verifica se a média é maior ou igual a 6.0 e menor que 7.5, se sim retorna 'C'
    elif media_aproveitamento >= 6.0 and media_aproveitamento < 7.5:
        return 'C'

    # Verifica se a média é menor que 6.0, se sim retorna 'D'
    elif media_aproveitamento < 6.0:
        return 'D'