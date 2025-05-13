```py
import random
import numpy as np

tasks = [5, 8, 4, 7, 6, 3, 9] 
facilities = [24, 30, 28]  
cost_matrix = [
    [10, 12, 9],
    [15, 14, 16],
    [8, 9, 7],
    [12, 10, 13],
    [14, 13, 12],
    [9, 8, 10],
    [11, 12, 13]
]

POP_SIZE = 6
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.2
GENERATIONS = 50

def generate_population():
    return [random.choices([1, 2, 3], k=len(tasks)) for i in range(POP_SIZE)]

def fitness(cur):
    total_cost = 0
    loads = [0, 0, 0] 
    
    for i, facility in enumerate(cur):
        facility_index = facility - 1
        loads[facility_index] += tasks[i]
        total_cost += tasks[i] * cost_matrix[i][facility_index]
    
    for i, load in enumerate(loads):
        if load > facilities[i]:
            total_cost += (load - facilities[i]) * 100
    
    return -total_cost  

def select(population):
    fitness_values = [fitness(chrom) for chrom in population]
    total_fitness = sum(fitness_values)
    probabilities = [f / total_fitness for f in fitness_values]
    return population[np.random.choice(len(population), p=probabilities)]

def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, len(tasks) - 1)
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]
    return parent1, parent2

def mutate(cur): 
    if random.random() < MUTATION_RATE:
        idx1, idx2 = random.sample(range(len(tasks)), 2)
        cur[idx1], cur[idx2] = cur[idx2], cur[idx1]
    return cur

def genetic_algorithm():
    population = generate_population()
    
    for generation in range(GENERATIONS):
        new_population = []
        
        for _ in range(POP_SIZE // 2):
            Parent1, Parent2 = select(population), select(population)
            Child1, Child2 = crossover(Parent1, Parent2)
            new_population.extend([mutate(Child1), mutate(Child2)])
        
        population = new_population

    best_solution = min(population, key=fitness)
    best_cost = -fitness(best_solution)
    return best_solution, best_cost

best_assignment, best_cost = genetic_algorithm()
print("Best Task Allocation:", best_assignment)
print("Minimum Production Cost:", best_cost)
```

# OUTPUT:
![image](https://github.com/user-attachments/assets/cbbd2753-88bb-427a-a426-55ab623a75f4)
