data = []
with open("/home/alimahfoud24/ALI/inputDay13.txt") as file:
    line = file.readline()
    while line:
        data.append(line.strip('\n').split(','))
        line = file.readline()
data2 = []
instruction = []
dots = set()
for i in range(len(data)):
    if data[i] == ['']:
        instruction.extend(data[(i+1):])
        data2.extend(data[:i])

data2 = [[int(x) for x in lst] for lst in data2]
for j in range(len(data2)):
    dots.add((data2[j][0], data2[j][1]))


for i in range(len(instruction)):
    for j in range(len(instruction[i])):
        Equal_Index = instruction[i][j].index('=')
        AXIS_Index = instruction[i][j].index('=')-1
        AXIS = instruction[i][j][AXIS_Index]
        Coordinates = int(instruction[i][j][(Equal_Index+1):])
    if AXIS == 'x':
        dots = {(x if x < Coordinates else (2*Coordinates-x), y,)
                for x, y in dots}
    elif AXIS == 'y':
        dots = {(x, y if y < Coordinates else (2*Coordinates-y),)
                for x, y in dots}
    break
Result = len(dots)
print('After completing just the first fold instruction on the trCoordinatesparent paper, there are: ',
      Result, ' visible dots.')
