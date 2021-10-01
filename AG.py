import csv
import random

filmesDict = {}
with open('filmes.csv', newline='') as csvfile:
    filmes = csv.reader(csvfile, delimiter=',', quotechar='|')
    for idx, row in enumerate(filmes): 
        # print(idx, row[4])
        filmesDict[idx] = row
        

# remove a primeira linha, que é referente a descrição do item da tabela

#filmesDict.pop(0, None)
#minutesPerDay = 240

# seleciona filmes aleatórios e cria o primeiro cromossomo aleatoriamente
# O primeiro filme a ser assistindo está no índice 0, o segundo no índice 1, e por aí vai...
# a soma de tempo dos filmes não pode ser maior que 240.


total = 93

def createsPop (n):
    pop = []
    for x in range(n):
        crm = []
        aux = []
        for y in range(total):
            rand = random.randint(1,total)
            while rand in aux:
                rand = random.randint(1,total)
            aux.append(rand)
            crm.append(rand)
        if (crm.index(13) < crm.index(36)):
            aux2 = crm.index(36)
            crm[crm.index(13)] = 36
            crm[aux2] = 13
        pop.append(crm)
    return pop
        
# def countDays (c):
#     contHoras = 0
#     contDias = 0

    
#     for idx in c:
#         row = filmesDict[idx]
#         hours = row[4]
#         print(hours)
#         countHours = countHours + hours 

generation = 4

for x in range(generation):
