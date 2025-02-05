# 50 Challenging Problems in Probability
# 2. Successive Wins
# To encourage Elmer’s promising tennis career, his father offers him a prize if he
# wins (at least) two tennis sets in a row in a three-set series to be played with
# his father and the club champion alternately: father-champion-father or
# champion-father-champion, according to Elmer’s choice. The champion is a better
# player than Elmer’s father. Which series should Elmer choose?


import random


def play_series(matches):
    match = lambda prob: random.choices(population=["W", "L"], cum_weights=[prob, 1])[0]
    result = "".join([match(prob) for prob in matches])
    return "WW" in result


def simulate():
    while True:
        father = random.random()
        champion = random.random()

        if father < champion:
            continue

        N = 1000
        fcf_wins = sum(play_series([father, champion, father]) for _ in range(N))
        cfc_wins = sum(play_series([champion, father, champion]) for _ in range(N))

        return fcf_wins / N, cfc_wins / N


T = 0
for _ in range(100):
    prob_fcf, prob_cfc = simulate()
    if prob_cfc > prob_fcf:
        T += 1

print(f"Out of 100 simulations CFC is more probable {T} times")
