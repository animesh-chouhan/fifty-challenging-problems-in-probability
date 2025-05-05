# 50 Challenging Problems in Probability
# 9. Craps
# The game of craps, played with two dice, is one of America’s fastest and most popular
# gambling games. Calculating the odds associated with it is an instructive exercise.

import random


# Simulation parameters
T = 100000  # Number of trials
random.seed(69)  # Seed for reproducibility

dice = [1, 2, 3, 4, 5, 6]
win = [7, 11]
loss = [2, 3, 12]


def simulate():
    gamble_roll = sum(random.choices(dice, k=2))

    if gamble_roll in win:
        return True
    elif gamble_roll in loss:
        return False
    else:
        last_roll = gamble_roll
        while True:
            new_roll = sum(random.choices(dice, k=2))
            if new_roll == last_roll:
                return True
            elif new_roll == 7:
                return False


# Simulate
W = 0
for _ in range(T):
    W += simulate()

# Win Percentage
print("Estimated probability:", W / T)
