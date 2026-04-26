# 🧬 Genetic Algorithm for Knapsack Problem

## 📌 Description

This project implements a **Genetic Algorithm (GA)** to solve the **Knapsack Problem**.
The goal is to select a subset of items such that:

* the **total weight does not exceed the knapsack capacity**
* the **total value is maximized**

---

## ⚙️ Input Format

The program expects input from the user:

* `C` — number of test cases (max 20)
* For each test case:

  * `N` — number of items (max 50)
  * `S` — Size of knapsack.
  * `N` lines with item data:

## 📤 Output Format

For each test case, the program prints:

* maximum value
* number of selected items
* list of selected items (weight, value)
* total weight

## 🧠 How It Works

### 1. Chromosome Representation

Each solution is encoded as a binary vector:

* `1` → item is included
* `0` → item is excluded

Example:

```
[1, 0, 1] → take item 1 and 3
```

---

### 2. Initial Population

A population of random chromosomes is generated.

---

### 3. Fitness Function

The fitness function calculates total value:

* if total weight > capacity → fitness = 0
* otherwise → sum of values

---

### 4. Selection

Tournament selection is used:

* a few individuals are randomly chosen
* the best one is selected

---

### 5. Crossover

Two parents exchange parts of their chromosomes to produce offspring.

---

### 6. Mutation

Random bits are flipped:

```
1 → 0
0 → 1
```

---

### 7. Elitism

The best individuals are preserved between generations.

---

### 8. Iteration

The process repeats for multiple generations to improve solutions.
