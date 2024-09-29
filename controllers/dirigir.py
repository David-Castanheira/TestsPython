def dirigir(a, b):
    if (a >= 18 and b == 's'):
        return 'Está apto para dirigir'
    elif (b =='n'):
        return 'Não está apto para dirigir'
    else:
        return 'Não tem idade suficiente'