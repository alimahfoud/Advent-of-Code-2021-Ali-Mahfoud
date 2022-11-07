import heapq
with open("/home/alimahfoud24/ALI/inputDay23.txt") as file:
    data = file.read().strip().split("\n")
hallway = data[1][1:12]
amphipods_1 = data[2][3:10:2]
amphipods_2 = data[3][3:10:2]
starting_position = [0, 0, 0, 0, 0, 0, 0, 0]
count_type = [0, 0, 0, 0]

for x in range(len(hallway)):
    if hallway[x] == '.':
        continue
    type_num = 'ABCD'.index(hallway[x])
    starting_position[type_num*2 + count_type[type_num]] = (x, -1, -1)
    count_type[type_num] += 1

for x, y in [(amphipods_1, 1), (amphipods_2, 2)]:
    for a in range(4):
        if x[a] == '.':
            continue
        type_num = 'ABCD'.index(x[a])
        starting_position[type_num*2 +
                          count_type[type_num]] = (-1, (a*2)+2, y)
        count_type[type_num] += 1

starting_situation = 0, tuple(starting_position)


def not_blocked(amphipods, index, destination_room):
    hallway, room, _ = amphipods[index]
    for a in range(8):
        if amphipods[a][0] == -1 or a == index:
            continue
        if (destination_room <= amphipods[a][0] <= max(hallway, room)) or (max(hallway, room) <= amphipods[a][0] <= destination_room):
            return False
    return True


def find_correct_room(position):
    energy, amphipods = position
    range_l = [0, 1, 3, 5, 7, 9, 10]
    for a, amphipod in enumerate(amphipods):
        type_num = a // 2
        location, room, y = amphipod
        if room == 2*type_num + 2 and location == -1:
            if y != 2:
                neighbour = amphipods[type_num*2 + (1 - a % 2)]
            elif y == 2 or ((neighbour[2], y) in [(1, 2), (2, 1)]):
                continue
        if True:
            if room == -1:
                energy_to_getOut = 0
            else:
                energy_to_getOut = y
            LOCATION = max(location, room)
            destination_room = 2*type_num + 2
            No_Block = True
            if room != -1 and y == 2:
                blocked = False
                for s in range(8):
                    if s == a:
                        continue
                    if amphipods[s][1] == room and amphipods[s][2] == 1:
                        blocked = True
                        break
                No_Block = not blocked
            if No_Block:
                other_type = False
                for r in range(8):
                    if r == a or r == type_num*2 + (1 - a % 2) or amphipods[r][1] == -1:
                        continue
                    if amphipods[r][1] == destination_room:
                        other_type = True
                        break
                if not other_type:
                    neighbour = amphipods[type_num*2 + (1 - a % 2)]
                    if neighbour[1] == (type_num + 1) * 2 and neighbour[2] != 1 and not_blocked(amphipods, a, destination_room):
                        moving_energy = pow(
                            10, type_num) * (abs(LOCATION - destination_room) + 1 + energy_to_getOut)
                        AMPHIPODS = list(amphipods)
                        AMPHIPODS[a] = (-1, destination_room, 1)
                        yield energy + moving_energy, tuple(AMPHIPODS)

                    elif neighbour[1] != (type_num + 1) * 2 and not any([amphipods[k][1] == destination_room for k in range(8) if k != a]) and not_blocked(amphipods, a, destination_room):
                        moving_energy = pow(
                            10, type_num) * (abs(LOCATION - destination_room) + 2 + energy_to_getOut)
                        AMPHIPODS = list(amphipods)
                        AMPHIPODS[a] = (-1, destination_room, 2)
                        yield energy + moving_energy, tuple(AMPHIPODS)
        if room == -1:
            continue
        if y == 2:
            blocked = False
            for t in range(8):
                if t == a:
                    continue
                if amphipods[t][1] == room and amphipods[t][2] == 1:
                    blocked = True
                    break
            if blocked:
                continue
        for goal_location in range_l:
            moving_energy = pow(10, type_num) * \
                (abs(room - goal_location) + (y))
            if not not_blocked(amphipods, a, goal_location):
                continue
            else:
                AMPHIPODS = list(amphipods)
                AMPHIPODS[a] = (goal_location, -1, -1)
            yield energy + moving_energy, tuple(AMPHIPODS)


def finish_line(amphipods):
    for a in range(8):
        amphipod = amphipods[a]
        location, room, y = amphipod
        if location != -1 or room != (a//2)*2 + 2:
            return False
    return True


location_visited = set()
Result = 0
Priority_Grid = [starting_situation]

while len(Priority_Grid) > 0:
    energy, amphipods = heapq.heappop(Priority_Grid)
    if amphipods in location_visited:
        continue
    location_visited.add(amphipods)
    if finish_line(amphipods):
        Result = energy
        break
    for moving in find_correct_room((energy, amphipods)):
        if not (moving[1] in location_visited):
            heapq.heappush(Priority_Grid, moving)

print('The least energy required to organize the amphipods is:', Result)
