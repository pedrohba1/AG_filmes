from csv import reader
from random import randint, uniform, sample

filmesDict = {}
with open('filmes.csv', newline='') as csvfile:
    filmes = reader(csvfile, delimiter=',', quotechar='|')
    for idx, row in enumerate(filmes): 
        filmesDict[idx] = [row[0], row[4], row[5], row[6]]

def createsPop (n):
    pop = []
    for x in range(n):
        crm = []
        aux = []
        for y in range(total):
            rand = randint(1,total)
            while rand in aux:
                rand = randint(1,total)
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

def fitness (c, time):
    countHours = 0
    countDays = 0
    films_per_day = []
    list_genres = []

    for idx in c:
        row = filmesDict[idx]
        hours = int(row[1])
        countHours = countHours + hours
        if countHours > time:
            countHours = hours
            countDays = countDays + 1
            genres = genre(films_per_day)
            list_genres.append(genres)
            films_per_day = []
        else:
            films_per_day.append(idx)
    
    return (countDays, sum(list_genres))

def genre(films):
    genres = []
    for i in films:
        genres.append(filmesDict[i][2])
        genres.append(filmesDict[i][3])
    genres = set(genres)
    if '' in genres:
        genres.remove('')
    return len(genres)

def mutation(pop, prob):
    list_new_cromossome = []
    for i in pop:
        prob_check = uniform(0, 1)
        if prob >= prob_check:
            new_cromossome = i.copy()
            change_positions = sample(range(0, len(i)), 2)
            new_cromossome[change_positions[0]], new_cromossome[change_positions[1]] = new_cromossome[change_positions[1]], new_cromossome[change_positions[0]]
            list_new_cromossome.append(new_cromossome)
    return list_new_cromossome

def worstCromossome(fitnessPop):
    fitnessPop = sorted(fitnessPop, key=lambda tup: tup[0], reverse=True)
    maxfit = fitnessPop[0][0]
    fitnessPop = [i for i in fitnessPop if i[0] == maxfit]
    crm = sorted(fitnessPop, key=lambda tup: tup[1])[0]
    return crm

def bestCromossome(fitnessPop):
    fitnessPop = sorted(fitnessPop, key=lambda tup: tup[0])
    minfit = fitnessPop[0][0]
    fitnessPop = [i for i in fitnessPop if i[0] == minfit]
    crm = sorted(fitnessPop, key=lambda tup: tup[1], reverse=True)[-1]
    return crm

def diary(crm, time):
    countDays = 1
    countHours = 0
    print("\n\n\nDiario de Filmes:")
    for i in crm:
        row = filmesDict[i]
        film, duration, gen1, gen2 = row[0], int(row[1]), row[2], row[3]
        countHours = countHours + duration
        if countHours > time:
            countHours = duration
            countDays = countDays + 1
            print('\n================\n')
            print("Dia " + str(countDays) + ":")
        else:
            print('')
        print("Filme: ", film)
        print("Duracao: ", duration)
        print("Genero:", gen1, gen2)

total = 93
time = 240
generation = 10
pop = createsPop(5)
print('pop:', pop)

for x in range(generation):
    MutatedCrm = []
    fitnessPop = []
    print('\n================\n')
    print('generation: ', x)
    
    MutatedCrm = mutation(pop, 1)
    # print('MutatedCRM: ', MutatedCrm)
    nMutated = len(MutatedCrm)
    # print('nMutated', nMutated)
    pop.extend(MutatedCrm)
    # print('extended pop: ', pop)
    
    for crm in pop:
        fitnessPop.append(fitness(crm, time))
    # print('fitnessPopLen: ', len(fitnessPop))
    print('fitnessPop: ', fitnessPop)

    for y in range(nMutated):
        # worstCrm = max(fitnessPop)
        worstCrm = worstCromossome(fitnessPop)
        print('worst: ', worstCrm)
        worstCrmIndex = fitnessPop.index(worstCrm)
        # print('worstIndex:  ', worstCrmIndex)
        pop.pop(worstCrmIndex)
        # print('pop-index: ', pop)
        fitnessPop.pop(worstCrmIndex)
        # print('fitnessPop-index: ',fitnessPop)
    
    bestCrm = min(fitnessPop)
    bestCrmIndex = fitnessPop.index(bestCrm)
    print('Melhor cromossomo da geração: ', pop[bestCrmIndex])
    print('Quantidade de dias: ', bestCrm[0])
    print('Quantidade de generos diferentes por dia: ', bestCrm[1])

print('Melhor cromossomo final: ', pop[bestCrmIndex])
print('Quantidade de dias final: ', bestCrm[0])
print('Quantidade de generos diferentes por dia final: ', bestCrm[1])

diary(pop[bestCrmIndex], time)