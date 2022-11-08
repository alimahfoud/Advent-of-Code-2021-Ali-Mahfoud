map = []
with open("/home/alimahfoud24/ALI/inputDay25.txt") as file:
    line = file.readline()
    while line:
        map.append(line.strip('\n'))
        line = file.readline()
MAP_d = {}
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == '>' or map[i][j] == 'v':
            MAP_d[(j, i)] = map[i][j]
height = len(map)
width = len(map[0])
Result = 0

while True:
    Result += 1
    MAP_d_copy1 = {}
    for (x, y), direction in MAP_d.items():
        if direction == '>':
            next_direction = ((x+1) % width), y
            if next_direction in MAP_d:
                MAP_d_copy1[(x, y)] = direction
            else:
                MAP_d_copy1[next_direction] = direction
        else:
            MAP_d_copy1[(x, y)] = direction
    MAP_d_copy2 = {}
    for (x, y), direction in MAP_d_copy1.items():
        if direction == 'v':
            next_direction = x, ((y+1) % height)
            if next_direction in MAP_d_copy1:
                MAP_d_copy2[(x, y)] = direction
            else:
                MAP_d_copy2[next_direction] = direction
        else:
            MAP_d_copy2[(x, y)] = direction
    if MAP_d_copy2 == MAP_d:
        break
    else:
        MAP_d = MAP_d_copy2
print('The first step on which no sea cucumbers move is:', Result)
