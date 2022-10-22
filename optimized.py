# Modules & Packages
import csv
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
                row.append((row[2] / 100) * row[1])
                if float(row[1]) > 0:
                    data.append(row)
            except:
                pass
        data.pop(0)
    return data


def sort_by_profit(data):
    return sorted(data, key=lambda x: x[3], reverse=True)


def find_best_combination_by_profit(sorted_data, max_cost):
    result = []
    best_combination = []
    active_cost = 0
    best_profit = 0
    for i in range(0, len(sorted_data) - 1):
        if active_cost + sorted_data[i][1] > max_cost:
            break
        else:
            active_cost += sorted_data[i][1]
            best_profit += sorted_data[i][3]
            best_combination.append(sorted_data[i])
    result.extend((best_combination, active_cost, best_profit))
    return result


def display_result(result):
    for item in result[0]:
        print(item[0])
    print(f"Coût total des actions : {result[1]}€")
    print(f"Gain sur 2 ans : {result[2]}€")
    print(f"Fini en {end - start} sec")


raw_data = get_data_from_csv('./data/dataset2_Python+P7.csv')
start = time.time()
sorted_data = sort_by_profit(raw_data)
best_combination = find_best_combination_by_profit(sorted_data, max_cost)
end = time.time()
display_result(best_combination)
