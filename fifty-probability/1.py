# 50 Challenging Problems in Probability
# 1. The Sock Drawer
# A drawer contains red socks and black socks.
# When two socks are drawn at random, the probability that both are red is 1/2.
# (a) How small can the number of socks in the drawer be?
# (b) How small if the number of black socks is even?

from itertools import combinations


def simulate(partb=False):
    for n in range(2, 100):
        for r in range(n + 1):
            b = n - r
            socks = ["R"] * r + ["B"] * b
            events = list(combinations(socks, 2))
            fave_events = [event for event in events if event.count("R") == 2]
            if len(events) == 2 * len(fave_events) and (not partb or b % 2 == 0):
                return n


print(f"Part A: {simulate(partb=False)}")
print(f"Part B: {simulate(partb=True)}")
# Part A: 4
# Part B: 21
