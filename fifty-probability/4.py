# 50 Challenging Problems in Probability
# 4. Trials until First Success
# On the average, how many times must a die be thrown until one gets a 6?

import random
from statistics import mean, stdev

sides = list(range(1, 7))


def simulate():
    n = 1
    while random.choice(sides) != 6:
        n += 1
    return n


# Simulation parameters
T = 100000  # Number of trials
random.seed(69)  # Seed for reproducibility


throws = [simulate() for _ in range(T)]
print(f"Average number of die throws: {mean(throws):.8f}")
print(f"Standard Deviation of throws: {stdev(throws):.8f}")
# Average number of die throws: 6.00175000
# Standard Deviation of throws: 5.47561017
