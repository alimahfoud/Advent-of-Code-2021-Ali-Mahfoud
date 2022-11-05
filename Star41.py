data = []
with open("/home/alimahfoud24/ALI/inputDay21.txt") as file:
    line = file.readline()
    while line:
        data.append(line.strip('\n'))
        line = file.readline()
player1_position = int(data[0][-1])
player2_position = int(data[1][-1])


def circular_track(position):
    while position > 10:
        position -= 10
    return position


rolls = 0
player1_score = 0
player2_score = 0

die = 0
while True:
    player1_position = circular_track(
        player1_position+(3*die+6))
    rolls += 3
    player1_score += player1_position
    die = die + 3
    if player1_score >= 1000:
        Result = player2_score*rolls
        break
    player2_position = circular_track(
        player2_position+(3*die+6))
    rolls += 3
    player2_score += player2_position
    die = die + 3
    if player2_score >= 1000:
        Result = player1_score*rolls
        break
print('By multiplying the score of the losing player by the number of times the die was rolled during the game, we get: ', Result)
