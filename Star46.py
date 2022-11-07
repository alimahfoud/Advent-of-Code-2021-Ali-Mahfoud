import heapq
with open("/home/alimahfoud24/ALI/inputDay23.txt") as file:
    data = file.read().strip().split("\n")

hallway = data[1][1:12]
amphipods_1 = data[2][3:10:2]

if len(data) == 5:
    amphipods_2 = "DCBA"
    amphipods_3 = "DBAC"
    amphipods_4 = data[3][3:10:2]
else:
    amphipods_2 = data[3][3:10:2]
    amphipods_3 = data[4][3:10:2]
    amphipods_4 = data[5][3:10:2]

starting_position = [0] * 16
count_type = [0, 0, 0, 0]

for x in range(len(hallway)):
    if hallway[x] == ".":
        continue
    type_num = "ABCD".index(hallway[x])
    starting_position[type_num*4 + count_type[type_num]] = (x, -1, -1)
    count_type[type_num] += 1

for x, y in [(amphipods_1, 1), (amphipods_2, 2), (amphipods_3, 3), (amphipods_4, 4)]:
    for a in range(4):
        if x[a] == ".":
            continue
        type_num = "ABCD".index(x[a])
        starting_position[type_num*4 + count_type[type_num]] = (-1, (a*2)+2, y)
        count_type[type_num] += 1

starting_situation = 0, tuple(starting_position)


def not_blocked(amphipods, index, destination_room):
    hallway, room, _ = amphipods[index]
    for a in range(16):
        if amphipods[a][0] == -1 or a == index:
            continue
        if (destination_room <= amphipods[a][0] <= max(hallway, room)) or (max(hallway, room) <= amphipods[a][0] <= destination_room):
            return False
    return True


def room_find(amphipods, target):
    S = [-1, -1, -1, -1]
    for a, amphipod in enumerate(amphipods):
        type = a // 4
        location, room, y = amphipod
        if room != -1:
            if room == target:
                S[4 - y] = type
            else:
                continue
    return S


def find_correct_room(position):
    energy, amphipods = position
    range_r = [2, 4, 6, 8]
    range_l = [0, 1, 3, 5, 7, 9, 10]
    for room in range_r:
        room_find(amphipods, room)
    for a, amphipod in enumerate(amphipods):
        type_num = a // 4
        location, room, y = amphipod
        if room == (type_num + 1) * 2 and location == -1:
            if y == 4:
                continue
            if room_find(amphipods, room)[:4-y] == [type_num] * (4 - y):
                continue
        else:
            energy_to_getOut = 0 if room == -1 else y
        LOCATION = max(location, room)
        destination_room = 2*type_num + 2
        No_Block = True
        if room != -1 and y > 1:
            blocked = False
            for s in range(16):
                if s == a:
                    continue
                if amphipods[s][1] == room and amphipods[s][2] < y:
                    blocked = True
                    break
            No_Block = not blocked

        if No_Block:
            other_type = False
            for r in range(16):
                if r // 4 == type_num or amphipods[r][1] == -1:
                    continue
                if amphipods[r][1] == destination_room:
                    other_type = True
                    break
            if not other_type:
                Yy = 4
                room_list = room_find(amphipods, destination_room)
                while room_list[4 - Yy] != -1:
                    Yy -= 1
                if not_blocked(amphipods, a, destination_room):
                    moving_energy = pow(
                        10, type_num) * (abs(LOCATION - destination_room) + Yy + energy_to_getOut)
                    AMPHIPODS = list(amphipods)
                    AMPHIPODS[a] = (-1, destination_room, Yy)
                    yield energy + moving_energy, tuple(AMPHIPODS)
        if room == -1:
            continue
        if y > 1:
            blocked = False
            for t in range(16):
                if t == a:
                    continue
                if amphipods[t][1] == room and amphipods[t][2] < y:
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
    for type_num in range(4):
        if room_find(amphipods, 2*type_num + 2) != [type_num] * 4:
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
