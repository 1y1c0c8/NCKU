import random
import math

def calculate_shortest_path_simulated_annealing(graph, temperature, cooling_rate, iterations):
    num_nodes = len(graph)
    current_path = list(range(num_nodes))
    best_path = current_path
    current_distance = 0
    best_distance = float('inf')

    for i in range(num_nodes):
        current_distance += graph[current_path[i]][current_path[(i + 1) % num_nodes]]
    
    for _ in range(iterations):
        new_path = current_path[:]
        a, b = random.sample(range(num_nodes), 2)
        new_path[a], new_path[b] = new_path[b], new_path[a]
        new_distance = 0
        for i in range(num_nodes):
            new_distance += graph[new_path[i]][new_path[(i + 1) % num_nodes]]
        
        if new_distance < current_distance or random.random() < math.exp((current_distance - new_distance) / temperature):
            current_path = new_path
            current_distance = new_distance
        
        if current_distance < best_distance:
            best_path = current_path
            best_distance = current_distance
        
        temperature *= cooling_rate

    return best_path, best_distance
