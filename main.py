import math

K = 40

def Probability(rating1, rating2): 
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400))

def EloRating(Ra, Rb, d):
    # To calculate the Winning
    # Probability of Player B
    Pb = Probability(Ra, Rb)
    # To calculate the Winning
    # Probability of Player A
    Pa = Probability(Rb, Ra)
    # Case -1 When Player A wins
    # Updating the Elo Ratings
    if (d == 1):
        Ra = Ra + K * (1 - Pa)
        Rb = Rb + K * (0 - Pb)
    # Case -2 When Player B wins
    # Updating the Elo Ratings
    else:
        Ra = Ra + K * (0 - Pa)
        Rb = Rb + K * (1 - Pb)
 

    return Ra, Rb


options = []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        options.append(
            [line.replace('\n', ''), 400]
        )

options_count = len(options)

for idx1 in range(options_count):
    for idx2 in range(idx1+1, options_count):
        choice = int(input(f'Что побеждает?: \n[1] {options[idx1][0]}\n[2] {options[idx2][0]}\nОтвет: '))
        options[idx1][1], options[idx2][1] = EloRating(options[idx1][1], options[idx2][1], choice)

options.sort(key=lambda x: x[1], reverse=True)

for option in options:
    print(option)