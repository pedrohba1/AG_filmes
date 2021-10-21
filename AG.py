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
            crm = restriction(crm)
        pop.append(crm)
    return pop

def restriction(crm):
    if (crm.index(13) < crm.index(36)):
        aux2 = crm.index(36)
        crm[crm.index(13)] = 36
        crm[aux2] = 13
    return crm

        
def fitness (c):
    countHours = 0
    countDays = 0

    
    for idx in c:
        row = filmesDict[idx]
        hours = int(row[4])
        countHours = countHours + hours 
        if (countHours > 240):
            countHours = hours
            countDays = countDays + 1
    
    return countDays

def mutation(cromossome, prob):
    prob_check = random.uniform(0, 1)
    if prob <= prob_check:
        change_positions = random.sample(range(0, len(cromossome)), 2)
        print('posicao: ',change_positions)
        cromossome[change_positions[0]], cromossome[change_positions[1]] = cromossome[change_positions[1]], cromossome[change_positions[0]]
        cromossome = restriction(cromossome)
    # return cromossome

populacao = createsPop(1)
print('pt1: ', populacao)
mutation(populacao[0], 0.4)
print('pt2: ', populacao)

generation = 4
pop = createsPop(3)
bestCrm = 1000
fitnessPop = []
MutatedCrm = []

for x in range(generation):
    for crm in pop:
        MutatedCrm = mutation(crm, 0.4)
        fitnessPop.append(fitness(crm))
    
    bestCrm = min(fitnessPop)
    print('Melhor cromossomo da geração: ', bestCrm)

print("Melhor cromossomo final: ", bestCrm)

