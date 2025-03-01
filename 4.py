"""4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP - R$67.836,43
• RJ - R$36.678,66
• MG - R$29.229,88
• ES - R$27.165,48
• Outros - R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora."""

def calcula_estados(faturamento_por_estado):

  faturamento_total = sum(faturamento_por_estado.values())

  percentuais = {}
  for estado, valor in faturamento_por_estado.items():
    percentuais[estado] = (valor / faturamento_total) * 100

  return percentuais

faturamento = {
  "SP": 67836.43,
  "RJ": 36678.66,
  "MG": 29229.88,
  "ES": 27165.48,
  "Outros": 19849.53
}

resultados = calcula_estados(faturamento)

for estado, percentual in resultados.items():
  print(f"{estado}: {percentual:.2f}%")