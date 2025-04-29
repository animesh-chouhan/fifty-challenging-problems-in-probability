# 50 Challenging Problems in Probability
# 5. Coin in Square
# In a common carnival game a player tosses a penny from a distance of about 5 feet onto the surface
# of a table ruled in 1-inch squares. If the penny (3/4 inch in diameter) falls entirely inside a
# square, the player receives 5 cents but does not get his penny back; otherwise he loses his penny.

import random


# Simulation parameters
T = 100000  # Number of trials
random.seed(69)  # Seed for reproducibility
table_length = 1
circle_radius = 3 / 8


def simulate(circle_center_x, circle_center_y):
    return (circle_radius <= circle_center_x <= table_length - circle_radius) and (
        circle_radius <= circle_center_y <= table_length - circle_radius
    )


# Simulate
W = 0
for _ in range(T):
    circle_center_x = random.random()
    circle_center_y = random.random()
    if simulate(circle_center_x, circle_center_y):
        W += 1

# Win Percentage
print(W / T)
