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
with open('./data/dataset1_Python+P7.csv', 'r') as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        try:
            row[1] = float(row[1])
            row[2] = float(row[2])
            row.append((row[2] / 100) * row[1])
            if float(row[1]) > 0:
                data.append(row)
        except:
            pass
    data.pop(0)

# traiter les données

# algo
sorted_data = sorted(data, key=lambda x: x[3], reverse=True)
print(sorted_data)
for i in range(0, len(sorted_data)-1):
    if active_cost + sorted_data[i][1] > max_cost:
        pass
    else:
        active_cost += sorted_data[i][1]
        best_profit += sorted_data[i][3]
        best_combination.append(sorted_data[i])

# affichage des résultats
end = time.time()
active_cost = 0
for item in best_combination:
    print(item)
    active_cost += item[1]
print(f"Coût total des actions : {active_cost}€")
print(f"Gain sur 2 ans : {best_profit}€")
print(f"Fini en {end-start} sec")

