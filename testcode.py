import re

texto = "21.5Cruzeiro"
numeros = re.findall(r'\d+\.?\d*', texto)

if numeros:
    numero_extraido = float(numeros[0])
    print("Número extraído:", numero_extraido)
else:
    print("Nenhum número encontrado na string.")