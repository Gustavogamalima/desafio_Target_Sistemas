import json

# 1. Importando o json contendo os dados do faturamento mensal
with open('dados.json', 'r') as f:
    faturamento_mensal = json.load(f)

# 2. Calculando o menor e o maior valor de faturamento ocorrido em um dia do mês
valores = [dia['valor'] for dia in faturamento_mensal]
menor_valor = min(valores)
maior_valor = max(valores)

print(f'Menor valor de faturamento: R$ {menor_valor:.2f}')
print(f'Maior valor de faturamento: R$ {maior_valor:.2f}')

# 3. Calculando a média mensal, ignorando os dias sem faturamento
dias_com_faturamento = [dia['valor'] for dia in faturamento_mensal if dia['valor'] != 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

# 4. Contando o número de dias no mês em que o valor de faturamento diário foi superior à média mensal
dias_acima_da_media = sum(1 for dia in dias_com_faturamento if dia > media_mensal)

print(f'Número de dias com faturamento acima da média mensal: {dias_acima_da_media}')
