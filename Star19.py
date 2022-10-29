nav_subsystem_data = []
with open("/home/alimahfoud24/ALI/inputDay10.txt") as file:
    line = file.readline()
    while line:
        nav_subsystem_data.append(line.strip('\n'))
        line = file.readline()
OPEN = '([{<'
CLOSE = ')]}>'
Scores = [3, 57, 1197, 25137]

total_score = 0
Open_Alone = []

for line in nav_subsystem_data:
    for char in line:
        if char in OPEN:
            Open_Alone.append(char)
        elif char in CLOSE:
            i = CLOSE.find(char)
            if Open_Alone[-1] != OPEN[i]:
                total_score += Scores[i]
                break
            else:
                del (Open_Alone[-1])

print('The total syntax error score for those errors is: ', total_score)
