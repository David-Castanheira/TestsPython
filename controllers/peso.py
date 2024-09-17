# Função de cálculo de peso com base na altura e sexo
def obter_peso(altura, sexo):
    # Verifica se é do sexo masculino
    if sexo == 'M':
        return (72.7 * altura) - 58 
    else:
        return (62.1 * altura) - 44.7