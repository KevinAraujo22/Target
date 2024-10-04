"""3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;"""

import json

def analisa_faturamento(arquivo_json):

  with open(arquivo_json, 'r') as f:
    dados = json.load(f)

  faturamentos = [dia['valor'] for dia in dados if 'valor' in dia]

  media_mensal = sum(faturamentos) / len(faturamentos)

  menor_valor = min(faturamentos)
  maior_valor = max(faturamentos)

  dias_acima_media = sum(1 for valor in faturamentos if valor > media_mensal)

  return menor_valor, maior_valor, dias_acima_media

arquivo = 'faturamento.json'
menor, maior, dias_acima = analisa_faturamento(arquivo)

print("Menor valor de faturamento:", menor)
print("Maior valor de faturamento:", maior)
print("Número de dias com faturamento acima da média:", dias_acima)
