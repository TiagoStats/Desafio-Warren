def is_numero_valido(tempo):

    try:

        (int (tempo))//1 == (int (tempo)) == False
    
    except Exception:

        return False

    return True

print("")
print("------------ DESAFIO 02 ------------")
print("")

maxAlunos = input("Número máximo de alunos atrasados: ")

while (maxAlunos.isnumeric() == False): # Neste caso permitindo apenas números naturais.

    print('\033[0;31mInsira um número válido.\033[m')

    maxAlunos = input("Número máximo de alunos atrasados: ")

listaChegada = []

while True:

    if (len(listaChegada) == 0):

        tempo = input("Insira o horário de chegada do 1º aluno: ")

        while (is_numero_valido(tempo) == False): # Neste caso permitindo números inteiros.

            print('\033[0;31mInsira um horário válido.\033[m')

            tempo = input("Insira o horário de chegada do 1º aluno: ")   

        listaChegada.append(int(tempo))

    else:

        maisAlunos = input("Existe mais algum aluno? [S/N] ")

        while (maisAlunos.upper() not in ['N','S']):

            print('\033[0;31mInsira "S" para Sim ou "N" para não.\033[m')

            maisAlunos = input("Existe mais algum aluno? [S/N] ")

        if (maisAlunos.upper() != "N"):

            tempo = input("Insira o horário de chegada do " + str(len(listaChegada)+1) + "º aluno: ")    

            while (is_numero_valido(tempo) == False): # Neste caso permitindo números inteiros.

                print('\033[0;31mInsira um horário válido.\033[m')

                tempo = input("Insira o horário de chegada do " + str(len(listaChegada)+1) + "º aluno: ")    

            listaChegada.append(int(tempo))

        else:

            break

atrasados = 0

for i in range(len(listaChegada)):

    if (listaChegada[i] > 0):

        atrasados += 1

if atrasados > int(maxAlunos):
    print("")
    print("-------------- RESULTADO --------------")
    print("")
    print("Aula cancelada. ")
    print("")
    print("Máximo de alunos atrasados definido: " + str(maxAlunos))
    print("Total de alunos atrasados: " + str(atrasados))
    print("")
    print("---------------------------------------")

else:
    print("")
    print("-------------- RESULTADO --------------")
    print("")
    print("Aula normal. ")
    print("")
    print("Máximo de alunos atrasados definido: " + str(maxAlunos))
    print("Total de alunos atrasados: " + str(atrasados))
    print("")
    print("---------------------------------------")


