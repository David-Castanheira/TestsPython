# Função de cálculo de dosagem de remédio com base na idade e peso
def calcular_dosagem(idade, peso):

     # Validações de idade e peso
    if idade < 0 and peso < 0:
        raise ValueError('A idade não pode ser menor que 0!')
    elif idade > 120 and peso >= 250:
        raise ValueError('A idade não pode ser maior que 120!')
    
    # Verifica se a idade é maior ou igual a 12
    if idade >= 12:
        # Verifica se a idade é maior ou igual a 60
        if idade >= 60:
            # Retorna a quantidade que deve ser ingerida
            return 1000
        else:
            # Em caso negativo, retorna outra quantidade que deve ser ingerida
            return 875
    else: 
        # Se idade for menor que 12, verifica se o o peso está entre 5 e 9 e retorna a quantidade que deve ser ingerida
        if peso >= 5 and peso <= 9:
            return 125
        # Verifica se o o peso está entre 9.1 e 16 e retorna a quantidade que deve ser ingerida
        elif peso >= 9.1 and peso <= 16:
            return 250
        # Verifica se o o peso está entre 16.1 e 24 e retorna a quantidade que deve ser ingerida
        elif peso >= 16.1 and peso <= 24:
            return 375
        # Verifica se o o peso está entre 24.1 e 30 e retorna a quantidade que deve ser ingerida
        elif peso >= 24.1 and peso <= 30:
            return 500
        # Por fim, verifica se o o peso está acima de 30 e retorna a quantidade que deve ser ingerida
        elif peso >= 30:
            return 750