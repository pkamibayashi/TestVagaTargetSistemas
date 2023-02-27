import json

# Lê o arquivo JSON com os dados do faturamento mensal
with open('faturamento.json', 'r') as f:
    dados = json.load(f)

# Inicializa as variáveis com os valores do primeiro dia
menor_valor = maior_valor = dados[0]['valor']
soma_valores = dados[0]['valor']
num_dias_acima_media = 0

# Percorre os dados do faturamento mensal
for dia in dados[1:]:
    valor = dia['valor']

    # Verifica se o valor do dia é menor que o menor valor registrado
    if valor < menor_valor:
        menor_valor = valor

    # Verifica se o valor do dia é maior que o maior valor registrado
    if valor > maior_valor:
        maior_valor = valor

    # Soma o valor do dia para calcular a média no final
    soma_valores += valor

# Calcula a média mensal excluindo os dias sem faturamento
num_dias = len(dados)
media = soma_valores / num_dias
num_dias_sem_faturamento = num_dias - len([dia for dia in dados if dia['valor'] != 0])
media_sem_faturamento = soma_valores / num_dias_sem_faturamento

# Conta o número de dias em que o faturamento foi superior à média mensal
for dia in dados:
    if dia['valor'] > media:
        num_dias_acima_media += 1

# Imprime os resultados
print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média: {num_dias_acima_media}")
print(f"Média mensal de faturamento: R${media:.2f}")
print(f"Média mensal de faturamento (excluindo dias sem faturamento): R${media_sem_faturamento:.2f}")
