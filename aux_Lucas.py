import csv
import random
# import numpy as np

filmesDict = {}
with open('filmes.csv', newline='') as csvfile:
    filmes = csv.reader(csvfile, delimiter=',', quotechar='|')
    for idx, row in enumerate(filmes): 
        # print(idx, row[4])
        filmesDict[idx] = (row[4], row[0])

filmesDict.pop(0, None)
minutesPerDay = 240

# seleciona filmes aleatórios e cria o primeiro cromossomo aleatoriamente
# O primeiro filme a ser assistindo está no índice 0, o segundo no índice 1, e por aí vai...
# a soma de tempo dos filmes não pode ser maior que 240.

toRandomizeDict = filmesDict

def createsPop (n):
    pop = []
    for _ in range(n):
        lista = list(range(1,93))
        random.shuffle(lista)
        pop.append(lista)
    return pop

def movie_name(cromossome, film):
    for i in range(len(cromossome)):
        cromossome[i] = film[cromossome[i]]
    return cromossome

def mutation(cromossome, prob):
    prob_check = random.uniform(0, 1)
    if prob <= prob_check:
        change_positions = random.sample(range(0, len(cromossome)), 2)
        cromossome[change_positions[0]], cromossome[change_positions[1]] = cromossome[change_positions[1]], cromossome[change_positions[0]]
    return old_cromossome

# print(movie_name(pop[0], filmesDict))

def new_mutation(pop, prob):
    list_new_cromossome = []
    for i in pop:
        prob_check = random.uniform(0, 1)
        if prob <= prob_check:
            new_cromossome = i.copy()
            change_positions = random.sample(range(0, len(i)), 2)
            print(i[change_positions[0]], i[change_positions[1]])
            new_cromossome[change_positions[0]], new_cromossome[change_positions[1]] = new_cromossome[change_positions[1]], new_cromossome[change_positions[0]]
            list_new_cromossome.append(new_cromossome)
    return list_new_cromossome

pop = createsPop(5)

for i in range(len(pop)):
    pop[i] = movie_name(pop[i], filmesDict)

list_new_cromossome = new_mutation(pop, 0.5)

print(len(list_new_cromossome))
print(pop[0])
print(list_new_cromossome[0])

# print(pop[0])
# print(len(pop[0]))



# print(movie_name(cromossome, filmesDict))