import numpy as np
with open("/home/alimahfoud24/ALI/inputDay5.txt") as file:
    rows = []
    row = file.readline()

    while row:
        row = row.strip('\n').split(' ')
        X1Y1 = [int(i) for i in row[0].split(',')]
        X2Y2 = [int(i) for i in row[2].split(',')]
        rows.append([X1Y1, X2Y2])
        row = file.readline()

s = (1000, 1000)
table = np.zeros(s)

for row in rows:
    if row[0][0] == row[1][0]:
        h = min(row[0][1], row[1][1])
        v = max(row[0][1], row[1][1])
        for i in range(h, v + 1):
            table[row[0][0]][i] += 1

    elif row[0][1] == row[1][1]:
        h = min(row[0][0], row[1][0])
        v = max(row[0][0], row[1][0])
        for i in range(h, v+1):
            table[i][row[0][1]] += 1
    else:
        if row[0][0] > row[1][0]:
            row = [row[1], row[0]]
        for point in range(row[1][0]-row[0][0] + 1):
            vertical = point if row[1][1] > row[0][1] else -point
            horizontal = point if row[1][0] > row[0][0] else -point
            table[row[0][0]+horizontal][row[0][1]+vertical] += 1

count = 0
for j in table:
    for y in j:
        if y > 1:
            count += 1

print('Two or more lines overlap at: ', count, ' points.')
