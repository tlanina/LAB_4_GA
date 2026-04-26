import random

def fitness(chromosome, items, capacity):
    total_weight = 0
    total_value = 0

    for gene, (w, v) in zip(chromosome, items):
        if gene == 1:
            total_weight += w
            total_value += v

    if total_weight > capacity:
        return 0

    return total_value

def generate_population(size, n_items):
    return [[random.randint(0, 1) for _ in range(n_items)]
        for _ in range(size)]

def selection(population, items, capacity, k=3):
    selected = []
    for _ in range(len(population)):
        tournament = random.sample(population, k)
        best = tournament[0]
        best_fit = fitness(best, items, capacity)

        for individual in tournament:
            current_fit = fitness(individual, items, capacity)

            if current_fit > best_fit:
                best = individual
                best_fit = current_fit

        selected.append(best)
    return selected


def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2


def mutation(chromosome, rate=0.01):
    for i in range(len(chromosome)):
        if random.random() < rate:
            chromosome[i] = 1 - chromosome[i]
    return chromosome


def genetic_algorithm(items, capacity, generations=100, pop_size=50):
    n_items = len(items)

    population = generate_population(pop_size, n_items)

    best_solution = None
    best_fitness = 0

    for _ in range(generations):
        def get_fitness(chromosome):
            return fitness(chromosome, items, capacity)

        population = sorted(population, key=get_fitness, reverse=True)
        new_population = population[:2]

        selected = selection(population, items, capacity)

        for i in range(0, pop_size - 2, 2):
            parent1 = selected[i]
            parent2 = selected[i + 1]

            child1, child2 = crossover(parent1, parent2)
            child1 = mutation(child1)
            child2 = mutation(child2)

            new_population.extend([child1, child2])

        population = new_population

        current_best = population[0]
        current_fitness = fitness(current_best, items, capacity)

        if current_fitness > best_fitness:
            best_fitness = current_fitness
            best_solution = current_best

    return best_solution, best_fitness

def solve():
    while True:
        try:
            C = int(input("Enter number of test cases (max 20): "))
            if 1 <= C <= 20:
                break
            else:
                print("Must be between 1 and 20. Try again.")
        except ValueError:
            print(" Enter a valid number!")

    for case_id in range(1, C + 1):
        print(f"\nTest Case {case_id}")

        while True:
            try:
                N = int(input("Enter number of items (max 50): "))
                if 1 <= N <= 50:
                    break
                else:
                    print("Must be between 1 and 50. Try again.")
            except ValueError:
                print("Enter a valid number!")

#CAPACITY
        while True:
            try:
                S = int(input("Enter knapsack capacity (>0): "))
                if S > 0:
                    break
                else:
                    print("Must be greater than 0. Try again.")
            except ValueError:
                print("Enter a valid number!")
# ITEMS
        items = []
        print("\nEnter items in format: weight value (like: 34 10)")

        for i in range(N):
            while True:
                try:
                    user_input = input(f"Item {i + 1} (weight value): ")
                    parts = user_input.split()

                    if len(parts) != 2:
                        print("Please enter EXACTLY two numbers: weight value")
                        continue

                    w, v = map(int, parts)

                    if w <= 0 or v <= 0:
                        print("Both must be positive!")
                        continue

                    items.append((w, v))
                    break
                except ValueError:
                    print("Invalid input! Example: 34 10")
        # RUN GA
        best_overall = None
        best_value = 0

        for _ in range(5):
            solution, value = genetic_algorithm(items, S)
            if value > best_value:
                best_value = value
                best_overall = solution

        #OUTPUT
        selected_items = [
            items[i] for i in range(N) if best_overall[i] == 1
        ]

        total_weight = sum(w for w, v in selected_items)

        print(f"\nResult for Test Case {case_id}")
        print(f"Maximum value: {best_value}")
        print(f"Number of selected items: {len(selected_items)}")

        print("\nSelected items (weight, value):")
        for w, v in selected_items:
            print(f"({w}, {v})")

        print(f"\nTotal weight: {total_weight} / {S}")
if __name__ == "__main__":
    solve()