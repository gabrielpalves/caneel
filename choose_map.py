from random import randint
from random import sample

# Lista de mapas jogáveis no competitivo
maps = ['Cache',
        'Dust II',
        'Nuke',
        'Mirage',
        'Inferno',
        'Insertion II',
        'Basalt',
        'Train',
        'Vertigo',
        'Overpass',
        'Ancient',
        'Office',
        'Agency',
        'Premier']

# For list of integers
lst1 = []

# For list of strings/chars
for i in range(1, len(maps)+1):
    print(str(i) + " - " + maps[i-1])

lst1 = [int(item) for item in input("Quais mapas você não quer jogar?").split()]

willPlay = []
for i in range(1, len(maps)+1):
    if (i not in lst1):
        willPlay.append(maps[i-1])

# Pergunta se quer readicionar algum mapa para compensar a indecisão do player
answers = input("Readicionar algum mapa excluído? (Digite: sim ou não)")

# Tem que readicionar mapa(s) se o user for realmente indeciso
if (answers == 'sim'):
    reAdd = []
    j = 0
    for i in range(len(maps)):
        if (maps[i] not in willPlay):
            j = j + 1
            reAdd.append(maps[i])
            aString = str(j) + " - " + maps[i]
            print(aString)

    if (j == 1):
        answers = input("Deseja jogar o mapa acima também? (Digite: sim ou não)")

        if (answers == 'sim'):
            willPlay.append(reAdd)
    else:
        lst2 = [int(item) for item in input("Informe quais dos mapas acima deseja considerar também: ").split()]
        for i in range(1, len(reAdd)+1):
            if (i in lst2):
                willPlay.append(reAdd[i-1])

# usuário define se vai jogar 1 mapa ou mais
print("Quantos mapas você deseja escolher?")
for i in range(1, len(willPlay)):
    if (i==1):
        print(str(i) + " - " + str(i) + " mapa")
    else:
        print(str(i) + " - " + str(i) + " mapas")

print(str(i+1) + " - Todos")
print(str(i+2) + " - Random")

txt = input("Quantos mapas você deseja escolher?")
n = int(txt)

if(n == i+2):
    nChoices = randint(1, len(willPlay))
elif(n == i+1):
    nChoices = len(willPlay)
else:
    for i in range(1, len(willPlay)+1):
        if i == n:
            nChoices = i
            break

# pega uma quantidade (informada pelo user ou gerada aleatoriamente) de mapas
sequence = [i for i in range(1, len(willPlay)+1)]

subset = sample(sequence, nChoices)  # select a subset without replacement
subset = sorted(subset)  # organiza a lista

print("Mapa(s) selecionado(s): ")
for i in range(1, len(subset)+1):
    print(str(i) + " - " + willPlay[i-1])
