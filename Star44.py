from collections import defaultdict
step = []
with open("/home/alimahfoud24/ALI/inputDay22.txt") as file:
    data = file.read().strip().split("\n")
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
    step.append((on_off, tuple(region)))


def intersect(edge1, edge2):
    intersection = []
    s = zip(edge1, edge2)
    for i, j in s:
        if i[1] >= j[0] and j[1] >= i[0]:
            intersection.append((max(i[0], j[0]), min(i[1], j[1])))
        else:
            return None
    x = tuple(intersection)
    return x


counts_cubes = defaultdict(int)
for i in range(len(step)):
    on_off, region = step[i]
    counts_cubes2 = defaultdict(int)
    for j in set(counts_cubes.keys()):
        on_off2 = counts_cubes[j] > 0
        intersection = intersect(region, j)
        if intersection == None:
            continue
        else:
            counts_cubes2[intersection] -= counts_cubes[j]
    if on_off:
        counts_cubes2[region] += 1
    for k in counts_cubes2:
        counts_cubes[k] += counts_cubes2[k]

Result = 0
for n in counts_cubes:
    i = 1
    for j in n:
        i *= abs(j[1] - j[0]) + 1
    Result += i * counts_cubes[n]


print('Considering all cubes, there are: ', Result, 'cubes that are ON.')
