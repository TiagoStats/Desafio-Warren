from itertools import combinations_with_replacement
print("")
print("------------ DESAFIO 03 ------------")
print("")
n = input("Número para atingir o somatório (apenas inteiros): ")

while (n.isnumeric() == False): # Neste caso permitindo apenas números naturais.

    print('\033[0;31mInsira um número válido (apenas inteiros).\033[m')

    n = input("Número para atingir o somatório (apenas inteiros): ")

listaElementos = [0]

while True:

    elemento = input("Insira o " + str(len(listaElementos)) + "º elemento inteiro. (Caso não tenha mais elementos apenas pressione ENTER) ")

    if (elemento != ""):

        while (elemento.isnumeric() == False):

            print('\033[0;31mInsira um número válido (apenas inteiros).\033[m')

            elemento = input("Insira o " + str(len(listaElementos)) + "º elemento inteiro. (Caso não tenha mais elementos apenas pressione ENTER) ")

        listaElementos.append(int(elemento))

    else:

        break


combinacoesPossiveis = combinations_with_replacement(listaElementos, len(listaElementos))

combinacoesValidas = []

for i in combinacoesPossiveis:

    if(len(combinacoesValidas))==0 or abs(sum(i) - int(n)) < abs(sum(combinacoesValidas[0]) - int(n)):

        combinacoesValidas = []

        lista = list(filter((0).__ne__, list(i)))

        combinacoesValidas.append(lista)

    elif (abs(sum(i)-int(n)) == abs(sum(combinacoesValidas[0])-int(n))):

        lista = list(filter((0).__ne__, list(i)))

        combinacoesValidas.append(lista)

resultado = []

for i in range(len(combinacoesValidas)):

    if (len(resultado) == 0):

        resultado.append(combinacoesValidas[i])

    elif (len(resultado[0]) > len(combinacoesValidas[i])):

        resultado.clear()

        resultado.append(combinacoesValidas[i])

    elif (len(resultado[0]) == len(combinacoesValidas[i])):

        resultado.append(combinacoesValidas[i])

print("")
print("-------------- RESULTADO --------------")
print("")
print(resultado)
print("")
print("---------------------------------------")
