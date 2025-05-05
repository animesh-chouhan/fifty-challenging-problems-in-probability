# 50 Challenging Problems in Probability
# 8: Perfect Bridge Hand
# We often read of someone who has been dealt 13 spades at bridge. With a well-shuffled pack
# of cards, what is the chance that you are dealt a perfect hand (13 of one suit)?

import random

# Simulation parameters
T = 1000000  # Number of trials
random.seed(69)  # Seed for reproducibility


# Suits and ranks
suits = ["♠️", "♥️", "♦️", "♣️"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# Create the deck
deck = [(rank, suit) for suit in suits for rank in ranks]


def simulate():
    hand = random.sample(deck, k=13)
    print(hand)
    suits_in_hand = [card[1] for card in hand]
    return all(s == suits_in_hand[0] for s in suits_in_hand)


# Simulate
W = 0
for _ in range(T):
    if simulate():
        break
        W += 1

# Win Percentage
print("Estimated probability:", W / T)
