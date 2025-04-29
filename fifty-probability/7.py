# Chuck-a-Luck is a gambling game often played at carnivals and gambling houses. A player may bet on any one of the numbers 1, 2, 3, 4, 5, 6. Three dice are rolled. If the player’s number appears on one, two, three of the dice, he receives respectively one, two, or three times his original stake plus his own money back; otherwise he loses his stake.

# Question: What is the player’s expected loss per unit stake?

import random


# Simulation parameters
T = 100000  # Number of trials
# random.seed(69)  # Seed for reproducibility

number = 13
total_rounds = 36


def simulate():
    players_choice = number
    roulette_roll = [random.randint(1, 38) for _ in range(total_rounds)]
    return roulette_roll.count(players_choice)


# Simulate
W = 0
for _ in range(T):
    rounds_won = simulate()
    gain = rounds_won * 36
    loss = (total_rounds - rounds_won) * -1
    net_gain = gain + loss
    W += net_gain
    # W += 1 if net_gain > 20 else 0

# Gain/Loss Percentage
print(W / T)
