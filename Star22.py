Octopus_Energy = []
with open("/home/alimahfoud24/ALI/inputDay11.txt") as file:
    line = file.readline()
    while line:
        Octopus_Energy.append([int(s) for s in line.strip('\n')])
        line = file.readline()
Length_list = len(Octopus_Energy)
Length_row = len(Octopus_Energy[0])
Cal = [-1, 0, 1]
Count = 0


def flashes(a, b):
    Octopus_Energy[a][b] = -1
    for x in Cal:
        for y in Cal:
            t = a+x
            v = b+y
            if 0 <= t < Length_list and 0 <= v < Length_row and Octopus_Energy[t][v] != -1:
                Octopus_Energy[t][v] += 1
                if Octopus_Energy[t][v] >= 10:
                    flashes(t, v)


while True:
    Count += 1
    for j in range(Length_list):
        for k in range(Length_row):
            Octopus_Energy[j][k] += 1
    for l in range(Length_list):
        for m in range(Length_row):
            if Octopus_Energy[l][m] == 10:
                flashes(l, m)
    light = True
    for n in range(Length_list):
        for o in range(Length_row):
            if Octopus_Energy[n][o] == -1:
                Octopus_Energy[n][o] = 0
            else:
                light = False
    if light:
        print('The first step during which all octopuses flash is: ', Count)
        break
