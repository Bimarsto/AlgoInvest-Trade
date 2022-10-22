# Modules & Packages
import csv
from itertools import combinations
import time

# Variables
max_cost = 500


def get_data_from_csv(path):
    data = []
    with open(path, 'r') as csvfile:
        file = csv.reader(csvfile)
        for row in file:
            try:
                row[1] = float(row[1])
                row[2] = float(row[2])
                if float(row[1]) > 0:
                    data.append(row)
            except:
                pass
    return data


def find_all_combinations(data, max_cost):
    all_combinations = []
    for n in range(len(data) + 1):
        for subset in combinations(data, n):
            active_combination_cost = 0
            active_combination_profit = 0
            for item in subset:
                active_combination_cost += item[1]
                active_combination_profit += (item[2] / 100) * item[1]
            if active_combination_cost <= max_cost:
                all_combinations.append([subset, active_combination_cost, active_combination_profit])
    return all_combinations


def find_best_profit(data):
    best_combination_profit = 0
    best_combination = []
    for combination in data:
        if combination[2] > best_combination_profit:
            best_combination_profit = combination[2]
            best_combination = combination
    return best_combination


def display_result(result):
    for item in result[0]:
        print(item[0])
    print(f"Coût total des actions : {result[1]}€")
    print(f"Gain sur 2 ans : {result[2]}€")
    print(f"Fini en {end-start} sec")


raw_data = get_data_from_csv('./data/actions.csv')
start = time.time()
all_combinations = find_all_combinations(raw_data, max_cost)
best_combination = find_best_profit(all_combinations)
end = time.time()
display_result(best_combination)
