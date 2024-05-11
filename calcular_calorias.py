def calcularCalorias(tempo, intensidade):
    # Suponhamos que a queima de calorias seja 5 por minuto, e a intensidade seja um numero inteiro
    caloriasPorMinuto = 5
    caloriasTotais = tempo * caloriasPorMinuto * intensidade

    return caloriasTotais

# Exemplo de uso
tempoAtividade = int(input("Digite o tempo de atividade (em minutos): ")) # em minutos
intensidadeAtividade = int(input('Digite a intensidade da atividade: ')) # fator de intensidade

caloriasGastas = calcularCalorias(tempoAtividade, intensidadeAtividade)
print(f"Você queimou {caloriasGastas} calorias durante a atividade")