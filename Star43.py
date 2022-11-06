import numpy as np
step = []
with open("/home/alimahfoud24/ALI/inputDay22.txt") as file:
    data = file.read().strip().split('\n')
for row in data:
    turn_OnOff = row.split(' ')
    if turn_OnOff[0] == 'on':
        turn_OnOff[0] = True
    else:
        turn_OnOff[0] = False
    on_off = turn_OnOff[0]
    region = []
    for xyz in turn_OnOff[1].split(","):
        xyz = xyz.split("..")
        region.append((int(xyz[0][2:]), int(xyz[1])))
    step.append((on_off, region))

on_off_table = np.zeros((101, 101, 101), dtype=bool)

for on_off, region in step:
    x, y, z = region
    if ((-50 > x[0] or x[1] > 50) or (-50 > y[0] or y[1] > 50) or (-50 > z[0] or z[1] > 50)):
        continue

    for i in range(x[0], x[1]+1):
        for j in range(y[0], y[1]+1):
            for k in range(z[0], z[1]+1):
                on_off_table[i, j, k] = on_off


Result = 0
for i in range(101):
    for j in range(101):
        for k in range(101):
            if on_off_table[i][j][k] == True:
                Result += 1
print('In the region x=-50..50,y=-50..50,z=-50..50, there are:',
      Result, 'cubes that are ON')
