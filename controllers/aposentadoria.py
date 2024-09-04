# Variáveis globais
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
    
    # Verifica se a idade é maior ou igual a 65, se sim requere aposentadoria
    if idade >= 65:
        return REQUERER
    # Verifica se o tempo de serviço é maior ou igual a 30, se sim requere aposentadoria
    elif tempo_de_servico >= 30:
        return REQUERER
    # Verifica se a idade é maior ou igual a 60 e o tempo de serviço é maior ou igual a 25, se sim requere aposentadoria
    elif idade >= 60 and tempo_de_servico >= 25:
        return REQUERER
    # Em nenhum caso válido, não requere aposentadoria
    return NAO_REQUERER