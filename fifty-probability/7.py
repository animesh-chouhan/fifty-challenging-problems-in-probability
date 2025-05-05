# 50 Challenging Problems in Probability
# 7. Curing the Compulsive Gambler
# Mr. Brown always bets a dollar on the number 13 at roulette against the advice of Kind Friend.
# To help cure Mr Brown of playing roulette, Kind Friend always bets Brown $20 at even money
# that Brown will be behind at the end of 36 plays. How is the cure working?

import random


# Simulation parameters
T = 100000  # Number of trials
random.seed(69)  # Seed for reproducibility

browns_number = 13
total_rounds = 36


def simulate():
    roulette_roll = [random.randint(1, 38) for _ in range(total_rounds)]
    return roulette_roll.count(browns_number)


# Simulate
brown_ahead = 0
brown_behind = 0
total_net_gain = 0

for _ in range(T):
    wins = simulate()
    net_gain = wins * 35 - (total_rounds - wins)
    total_net_gain += net_gain
    if net_gain >= 0:
        brown_ahead += 1
    else:
        brown_behind += 1

# Final results
expected_gain = total_net_gain / T
fraction_ahead = brown_ahead / T
fraction_behind = brown_behind / T
kind_friend_expected_gain = 20 * (fraction_behind - fraction_ahead)

print("Mr. Brown expected net gain per session:", expected_gain)
print("Fraction of times Mr. Brown is ahead:   ", fraction_ahead)
print("Fraction of times Mr. Brown is behind:  ", fraction_behind)
print("Kind Friend's expected gain per bet:    ", kind_friend_expected_gain)
