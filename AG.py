import csv
import random

filmesDict = {}
with open('filmes.csv', newline='') as csvfile:
    filmes = csv.reader(csvfile, delimiter=',', quotechar='|')
    for idx, row in enumerate(filmes): 
        # print(idx, row[4])
        filmesDict[idx] = row
        


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
    countDays = 1

    
    for idx in c:
        row = filmesDict[idx]
        hours = int(row[4])
        countHours = countHours + hours 
        if (countHours > 240):
            countHours = hours
            countDays = countDays + 1
    
    return countDays



def new_mutation(pop, prob):
    list_new_cromossome = []
    for i in pop:
        prob_check = random.uniform(0, 1)
        if prob >= prob_check:
            new_cromossome = i.copy()
            change_positions = random.sample(range(0, len(i)), 2)
            #print(i[change_positions[0]], i[change_positions[1]])
            new_cromossome[change_positions[0]], new_cromossome[change_positions[1]] = new_cromossome[change_positions[1]], new_cromossome[change_positions[0]]
            list_new_cromossome.append(new_cromossome)
    return list_new_cromossome


generation = 8000
pop = createsPop(500)
#print('pop: ', pop)

for x in range(generation):
    MutatedCrm = []
    fitnessPop = []
    print('generation: ', x)
    
    MutatedCrm = new_mutation(pop, 0.4)
    #print('MutatedCRM: ', MutatedCrm)
    nMutated = len(MutatedCrm)
    #print('nMutated', nMutated)
    pop.extend(MutatedCrm)
    #print('extended pop: ', pop)
    
    for crm in pop:
        fitnessPop.append(fitness(crm))
    #print('fitnessPopLen: ', len(fitnessPop))
    #print('fitnessPop: ', fitnessPop)

    for y in range(nMutated):
        worstCrm = max(fitnessPop)
        #print('worst: ', worstCrm)
        worstCrmIndex = fitnessPop.index(worstCrm)
        #print('worstIndex:  ', worstCrmIndex)
        pop.pop(worstCrmIndex)
        #print('pop-index: ', pop)
        fitnessPop.pop(worstCrmIndex)
        #print('fitnessPop-index: ',fitnessPop)
    
    bestCrm = min(fitnessPop)
    bestCrmIndex = fitnessPop.index(bestCrm)
    print('Melhor cromossomo da geração: ', pop[bestCrmIndex])
    print('Quantidade de dias: ', bestCrm)

print('Melhor cromossomo final: ', pop[bestCrmIndex])
print('Quantidade de dias final: ', bestCrm)

