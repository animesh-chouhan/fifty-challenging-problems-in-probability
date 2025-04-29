# Chuck-a-Luck is a gambling game often played at carnivals and gambling houses.
# A player may bet on any one of the numbers 1, 2, 3, 4, 5, 6. Three dice are rolled.
# If the player’s number appears on one, two, three of the dice, he receives respectively
# one, two, or three times his original stake plus his own money back; otherwise he loses his stake.
# Question: What is the player’s expected loss per unit stake?

import random


# Simulation parameters
T = 100000  # Number of trials
random.seed(69)  # Seed for reproducibility

dice = [1, 2, 3, 4, 5, 6]


def simulate():
    players_choice = random.choice(dice)
    gamble_roll = random.choices(dice, k=3)
    return gamble_roll.count(players_choice)


# Simulate
W = 0
for _ in range(T):
    gain_loss = simulate()
    W += gain_loss if gain_loss else -1

# Gain/Loss Percentage
print(W / T)
