# 50 Challenging Problems in Probability
# 3. The Flippant Juror
# A three-man jury has two members each of whom independently has probability p of
# making the correct decision and a third member who flips a coin for each decision
# (majority rules). A one-man jury has probability p of making the correct decision.

import random


def make_decision(members):
    decide = lambda prob: random.choices(["Y", "N"], cum_weights=[prob, 1])[0]
    result = "".join([decide(prob) for prob in members])
    return result.count("Y") >= 2


def simulate(p, N):
    flippant_juror = sum(make_decision([p, p, 0.5]) for _ in range(N))
    p_one_man = p
    return flippant_juror / N, p_one_man


# Simulation parameters
T = 100  # Number of trials
N = 10000  # Number of decisions per trial
random.seed(42)  # Seed for reproducibility

total_error = 0
for _ in range(T):
    juror_prob = random.random()
    prob_flippant, prob_one = simulate(juror_prob, N)
    total_error += abs(prob_flippant - juror_prob)

avg_error = total_error / T
print(f"Average error between the two juries: {avg_error:.8f}")
# Average error between the two juries: 0.00327437
