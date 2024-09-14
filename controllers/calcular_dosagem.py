def calcular_dosagem(idade, peso):
    if idade >= 12:
        if idade >= 60:
            return 1000
        else:
            return 875
    else: 
        if peso >= 5 and peso <= 9:
            return 125
        elif peso >= 9.1 and peso <= 16:
            return 250
        elif peso >= 16.1 and peso <= 24:
            return 375
        elif peso >= 24.1 and peso <= 30:
            return 500
        elif peso >= 30:
            return 750
    if idade < 0 and peso < 0:
        raise ValueError('A idade não pode ser menor que 0!')
    elif idade > 120 and peso >= 250:
        raise ValueError('A idade não pode ser maior que 120!')