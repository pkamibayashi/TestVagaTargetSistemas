# Definindo os valores de faturamento por estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calculando o faturamento total
total = sum(faturamento.values())

# Calculando e imprimindo o percentual de representação de cada estado
for estado, valor in faturamento.items():
    percentual = valor / total * 100
    print(f'{estado}: {percentual:.2f}%')
