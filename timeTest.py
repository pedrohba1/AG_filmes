def filmsDict():
    filmesDict = {}
    with open('filmes.csv', newline='') as csvfile:
        filmes = reader(csvfile, delimiter=',', quotechar='|')
        for idx, row in enumerate(filmes): 
            filmesDict[idx] = [row[0], row[4], row[5], row[6]]
    return filmesDict

def createsPop (n, total):
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

def fitness (c, time, filmesDict):
    #A funcao fitness calcula quantidade de dias que demoram para assistir todos os 
    #filmes e a soma dos gêneros que é possível assistir em um único dia

    countHours = 0
    countDays = 1
    films_per_day = []
    list_genres = []

    for idx in c:
        row = filmesDict[idx]
        hours = int(row[1])
        countHours = countHours + hours
        if countHours > time:
            countHours = hours
            countDays = countDays + 1
            genres = genre(films_per_day, filmesDict)
            list_genres.append(genres)
            films_per_day = []
        else:
            films_per_day.append(idx)
    
    return (countDays, sum(list_genres))

def genre(films, filmesDict):
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
            list_new_cromossome.append(new_cromossome)
    return list_new_cromossome

def worstCromossome(fitnessPop):
    #Pior Cromossomo: 1º: Mais dias, 2º: Menos gêneros

    #Sort Decrescente do 1º valor da tupla do fitnessPop
    fitnessPop = sorted(fitnessPop, key=lambda tup: tup[0], reverse=True)
    #Pegar os dias do pior cromossomo
    maxfit = fitnessPop[0][0]
    #Cortar a lista para pegar todos os cromossomos com pior dia
    fitnessPop = [i for i in fitnessPop if i[0] == maxfit]
    #Pegar o cromossomo com menor quantidade de gêneros somados
    crm = sorted(fitnessPop, key=lambda tup: tup[1])[0]
    return crm

def bestCromossome(fitnessPop):
    #Melhor cromossomo: 1º Menos dias, 2º Mais gêneros

    fitnessPop = sorted(fitnessPop, key=lambda tup: tup[0])
    minfit = fitnessPop[0][0]
    fitnessPop = [i for i in fitnessPop if i[0] == minfit]
    crm = sorted(fitnessPop, key=lambda tup: tup[1], reverse=True)[-1]
    return crm

def diary(crm, bestDays, time, filmesDict):

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

def main(total, time, generation, popSize):

    filmesDict = filmsDict()
    pop = createsPop(popSize, total)
    # print('pop:', pop)

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
            fitnessPop.append(fitness(crm, time, filmesDict))
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
        
        # bestCrm = min(fitnessPop)
        bestCrm = bestCromossome(fitnessPop)
        bestCrmIndex = fitnessPop.index(bestCrm)
        print('Melhor cromossomo da geração: ', pop[bestCrmIndex])
        print('Quantidade de dias: ', bestCrm[0])
        print('Quantidade de generos diferentes por dia: ', bestCrm[1])

    print('Melhor cromossomo final: ', pop[bestCrmIndex])
    print('Quantidade de dias final: ', bestCrm[0])
    print('Quantidade de generos diferentes por dia final: ', bestCrm[1])

    diary(pop[bestCrmIndex], bestCrm[0], time, filmesDict)

from timeit import default_timer as timer
from csv import reader
from random import randint, uniform, sample
for _ in range(it):
    start = timer()

    #Mudar os parametros it(quantidade de testes), generation(numero de geracoes), popSize(tamanho da populacao)
    #Lista: lista de tempos (em s) de cada teste
    lista = []
    it = 10
    total = 93
    time = 240
    generation = 20
    popSize = 5

    main(total, time, generation, popSize)
    end = timer()
    time = end - start
    lista.append(time)

from statistics import stdev
mean = sum(lista)/it
std = stdev(lista)
print("\n\nIteracao: ", it)
print("Tempo:", lista)
print("Media: ", mean)
print("Desvio Padrao: ", std)
