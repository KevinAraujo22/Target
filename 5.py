"""5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;"""

def inverter_string(texto):
  texto_invertido = ""
  for i in range(len(texto) - 1, -1, -1):
    texto_invertido += texto[i]
  return texto_invertido

texto = input("Digite uma palavra ou frase: ")
resultado = inverter_string(texto)
print("Texto invertido:", resultado)