# Modules & Packages
import csv
import itertools
import time

# Variables
data = []
max_cost = 500
best_combination = []
active_cost = 0
active_profit = 0
best_profit = 0

# choisir le fichier csv
# importer les données dans un tableau
start = time.time()
with open('./data/actions.csv', 'r') as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        try:
            row[1] = float(row[1])
            row[2] = float(row[2])
        except:
            pass

        data.append(row)
    data.pop(0)

# traiter les données

# algo
    # Trouver toutes les combinaisons
for n in range(0, len(data)-1):
    for subset in itertools.combinations(data, n):
        active_cost = 0
        active_profit = 0
        for item in subset:
            active_cost += item[1]
            active_profit += (item[2] / 100) * item[1]
        if 0 < active_cost <= max_cost and active_profit > best_profit:
            best_profit = active_profit
            best_combination = subset

# affichage des résultats
end = time.time()
active_cost = 0
for item in best_combination:
    print(item[0])
    active_cost += item[1]
print(f"Coût total des actions : {active_cost}€")
print(f"Gain sur 2 ans : {best_profit}€")
print(f"Fini en {end-start} sec")

