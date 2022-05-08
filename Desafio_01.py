from datetime import datetime

print("")
print("------------ DESAFIO 01 ------------")
print("")
print("Tempo médio de execução: 30 segundos.")
print("")

inicio = datetime.today()

reversiveis_impares = []

reversiveis_com_somatorio_menor_milhao = []

resultado = ""

# --------- Funções ----------

def inverter_numero(num):

    return int(str(num)[::-1])

def is_impar(num):

    if (num % 2 == 0):

        return False

    else:

        return True

# ----------------------------

for i in range(1000000):

    if(is_impar(i+1 + inverter_numero(i+1)) and ((i+1)%10 != 0) and (inverter_numero(i+1)%10 != 0)):

        reversiveis_impares.append(int(i+1))

for i in range(len(reversiveis_impares)):

    if((reversiveis_impares[i] + inverter_numero(reversiveis_impares[i])) < 1000000):

        reversiveis_com_somatorio_menor_milhao.append(reversiveis_impares[i])

for i in range(len(reversiveis_com_somatorio_menor_milhao)):

    if(str(inverter_numero(reversiveis_com_somatorio_menor_milhao[i])) not in resultado):

        resultado += str(reversiveis_com_somatorio_menor_milhao[i]) + " - "

resultado += "FIM"

print("Resultado:")
print("")
print(resultado)
print("")
print("Observação: Caso você não esteja consguindo ver todo o resultado, \nverique nas configurações da sua IDE o limite de linhas configurado\nno buffer do seu terminal.")
print("---------------------------------------")
print("")





