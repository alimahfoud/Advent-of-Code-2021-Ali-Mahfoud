nav_subsystem_data = []
with open("/home/alimahfoud24/ALI/inputDay10.txt") as file:
    line = file.readline()
    while line:
        nav_subsystem_data.append(line.strip('\n'))
        line = file.readline()
OPEN = '([{<'
CLOSE = ')]}>'
Scores = [1, 2, 3, 4]
Incomplete_lines = []

for line in nav_subsystem_data:
    Open_Alone = []
    corrupted_lines = False
    for char in line:
        if char in OPEN:
            Open_Alone.append(char)
        elif char in CLOSE:
            i = CLOSE.find(char)
            if Open_Alone[-1] != OPEN[i]:
                corrupted_lines = True
                break
            else:
                del (Open_Alone[-1])
    if corrupted_lines == False:
        Incomplete_lines.append(''.join(Open_Alone))

points = []
for line in Incomplete_lines:
    total_score = 0
    for j in line[::-1]:
        total_score *= 5
        total_score += Scores[OPEN.find(j)]
    points.append(total_score)

Result = sorted(points)[len(points)//2]
print('The middle score is : ', Result)
