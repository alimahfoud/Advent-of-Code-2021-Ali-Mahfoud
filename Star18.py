height_map = []
with open("/home/alimahfoud24/ALI/inputDay9.txt") as file:
    row = file.readline()

    while row:
        data = [int(x) for x in row.strip('\n')]
        height_map.append(data)
        row = file.readline()
map = len(height_map)
line = len(height_map[0])
vertical = [-1, 0, 1, 0]
horizontal = [0, 1, 0, -1]

Basin = []
B = set()
for x in range(map):
    for y in range(line):
        if (x, y) not in B and height_map[x][y] != 9:
            S = 0
            NEW = []
            NEW.append((x, y))
            while NEW:
                (x, y) = NEW.pop()
                if (x, y) in B:
                    continue
                B.add((x, y))
                S += 1
                for k in range(len(vertical)):
                    offset1 = x + vertical[k]
                    offset2 = y + horizontal[k]
                    if 0 <= offset1 < map and 0 <= offset2 < line and height_map[offset1][offset2] != 9:
                        NEW.append((offset1, offset2))
            Basin.append(S)
Basin.sort()
Result = Basin[-1]*Basin[-2]*Basin[-3]

print('When we multiply together the sizes of the three largest basins, we get: ', Result)
