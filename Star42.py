import functools
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


@functools.lru_cache(maxsize=None)
def get_winner(player1_position, player2_position, player1_score,  player2_score):
    player1_universes = 0
    player2_universes = 0
    for x in (1, 2, 3):
        for y in (1, 2, 3):
            for z in (1, 2, 3):
                player1_current_positon = circular_track(
                    player1_position+x+y+z)
                player1_current_positon_score = player1_score+player1_current_positon
                if player1_current_positon_score >= 21:
                    player1_universes += 1
                else:
                    i, j = get_winner(
                        player2_position, player1_current_positon, player2_score,  player1_current_positon_score)
                    player1_universes += j
                    player2_universes += i
    return player1_universes, player2_universes


Winning_Universes = get_winner(player1_position, player2_position, 0,  0)
if Winning_Universes[0] > Winning_Universes[1]:
    print('Player 1 is the winner and he wins in:',
          Winning_Universes[0], 'universes.')
else:
    print('Player 2 is the winner and he wins in:',
          Winning_Universes[1], 'universes.')
