from csv import reader
from random import randint, uniform, sample
import time as timer

start = timer.time()


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
    if (crm.index(12) < crm.index(35)):
        aux2 = crm.index(35)
        crm[crm.index(12)] = 35
        crm[aux2] = 12
    return crm

def fitness (c, time):
    #A funcao fitness recebe um cromossomo e o tempo diário limite (no caso 4 horas) e calcula a quantidade 
    # de dias necessários para assistir aos filmes do cromossomo crm e a soma da diversidade diária 
    # de gêneros

    #contador de horas
    countHours = 0
    #contador de dias
    countDays = 1
    #listas para controle de diversidade diária de gêneros
    films_per_day = []
    list_genres = []
    #para cada filme do cromossomo
    for idx in c:
        #recupera tempo de durção do filme
        row = filmesDict[idx]
        hours = int(row[1])
        #acrescenta este tempo de duração ao contador de horas
        countHours = countHours + hours
        #se o contador passa do tempo limite
        if countHours > time:
            #contador de horas é igualado ao tempo de duração do filme (filme atual entra no dia seguinte)
            countHours = hours
            #contador de dias é incrementado
            countDays = countDays + 1
            #retorna a quantidade diferentes de gênero deste dia
            genres = genre(films_per_day)
            #acrescenta esta quantidade à lista de diversidade diária de gêneros
            list_genres.append(genres)
            films_per_day = []
        #cai no else se o contador não passou ainda do tempo limite
        else:
            films_per_day.append(idx)
    #retorna o número de dias do cromossomo e a soma da diversidade diária de gêneros
    return (countDays, sum(list_genres))

def genre(films):
    # Retorna a quantidade de generos diferentes assistidos em um dia

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
            new_cromossome = restriction(new_cromossome)
            list_new_cromossome.append(new_cromossome)
    return list_new_cromossome

def worstCromossome(fitnessPop):
    # O pior indivíduo é aquele com, primeiramente, um maior número de dias e, segundamente, uma menor 
    # diversidade diária de gêneros

    #Ordena decrescentemente a lista de fitness com base no número de dias
    fitnessPop = sorted(fitnessPop, key=lambda tup: tup[0], reverse=True)
    #Recupera o maior número de dias presente na população
    maxfit = fitnessPop[0][0]
    #Recupera todos os indivíduos com o pior número de dias
    fitnessPop = [i for i in fitnessPop if i[0] == maxfit]
    #Recupera, dentre os indivíduos com o pior número de dias, o com a menor diversidade diárira de gêneros
    crm = sorted(fitnessPop, key=lambda tup: tup[1])[0]
    return crm

def bestCromossome(fitnessPop):
    #Melhor cromossomo: 1º Menos dias, 2º Mais gêneros

    fitnessPop = sorted(fitnessPop, key=lambda tup: tup[0])
    minfit = fitnessPop[0][0]
    fitnessPop = [i for i in fitnessPop if i[0] == minfit]
    crm = sorted(fitnessPop, key=lambda tup: tup[1], reverse=True)[-1]
    return crm

def diary(crm, bestDays, time):

    countDays = 1
    countHours = 0
    print("\n\nDiario de Filmes:")
    print('\n================\n')
    print("Dia 1:\n")
    for i in crm:       
        row = filmesDict[i]
        film, duration, gen1, gen2 = row[0], int(row[1]), row[2], row[3]
        countHours = countHours + duration
        if countHours > time:        
            countHours = duration
            countDays = countDays + 1
            print('\n================\n')
            print("Dia " + str(countDays) + ":\n")
        else:
            print('')
        
        print("Filme: ", film)
        print("Duracao: ", duration)
        print("Genero:", gen1, gen2)

total = 93
time = 240
generation = 600
pop = createsPop(500)
# print('pop:', pop)

for x in range(generation):
    MutatedCrm = []
    fitnessPop = []
    print('\n================\n')
    print('generation: ', x)
    
    MutatedCrm = mutation(pop, 0.6)
    # print('MutatedCRM: ', MutatedCrm)
    nMutated = len(MutatedCrm)
    # print('nMutated', nMutated)
    pop.extend(MutatedCrm)
    # print('extended pop: ', pop)
    
    for crm in pop:
        fitnessPop.append(fitness(crm, time))
    # print('fitnessPopLen: ', len(fitnessPop))
    # print('fitnessPop: ', fitnessPop)

    for y in range(nMutated):
        # worstCrm = max(fitnessPop)
        worstCrm = worstCromossome(fitnessPop)
        # print('worst: ', worstCrm)
        worstCrmIndex = fitnessPop.index(worstCrm)
        # print('worstIndex:  ', worstCrmIndex)
        pop.pop(worstCrmIndex)
        # print('pop-index: ', pop)
        fitnessPop.pop(worstCrmIndex)
        # print('fitnessPop-index: ',fitnessPop)
    
    # bestCrm = min(fitnessPop)
    bestCrm = bestCromossome(fitnessPop)
    bestCrmIndex = fitnessPop.index(bestCrm)
    print('Melhor cromossomo da geração: ', pop[bestCrmIndex])
    print('Quantidade de dias: ', bestCrm[0])
    print('Quantidade de generos diferentes por dia: ', bestCrm[1])

print('Melhor cromossomo final: ', pop[bestCrmIndex])
print('Quantidade de dias final: ', bestCrm[0])
print('Quantidade de generos diferentes por dia final: ', bestCrm[1])




diary(pop[bestCrmIndex], bestCrm[0], time)

end = timer.time()

print(f"Runtime of the program is {end - start}")
