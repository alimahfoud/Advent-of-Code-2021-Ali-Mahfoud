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
n = 0
Result = 0
for i in range(map):
    assert len(height_map[i]) == line
    for j in range(line):
        n = 1
        for k in range(len(vertical)):
            offset1 = i + vertical[k]
            offset2 = j + horizontal[k]
            if 0 <= offset1 < map and 0 <= offset2 < line and height_map[offset1][offset2] <= height_map[i][j]:
                n = 0
        if n > 0:
            Result += height_map[i][j]+1

print('The sum of the risk levels of all low points on the heightmap is: ', Result)
