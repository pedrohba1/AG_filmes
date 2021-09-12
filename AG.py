import csv
import random

filmesDict = {}
with open('filmes.csv', newline='') as csvfile:
    filmes = csv.reader(csvfile, delimiter=',', quotechar='|')
    for idx, row in enumerate(filmes): 
        # print(idx, row[4])
        filmesDict[idx] = row[4]

minutesPerDay = 240



# seleciona filmes aleatórios e cria os primeiros cromossomos aleatoriamente.
# O primeiro filme a ser assistindo está no índice 0, o segundo no índice 1, e por aí vai...
# a soma de tempo dos filmes não pode ser maior que 240.

toRandomizeDict = filmesDict

cromossome = []
while(len(list(toRandomizeDict.keys())) != 0 ):
    randMovieKey = random.choice(list(filmesDict.keys()))
    toRandomizeDict.pop(randMovieKey)
    cromossome.append(randMovieKey)

print(cromossome)