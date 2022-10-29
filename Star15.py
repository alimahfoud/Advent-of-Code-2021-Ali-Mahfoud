with open("/home/alimahfoud24/ALI/inputDay8.txt") as file:
    data = [row for row in file.read().strip().split('\n')]
    outputs = [row.split('|')[1].strip().split(' ') for row in data]


appearances = 0
known_patterns = [2, 3, 4, 7]

for value in outputs:
    for v in value:
        if (len(v)) in known_patterns:
            appearances += 1

print('Digits 1, 4, 7, or 8 appear ', appearances, 'times in the output values')
