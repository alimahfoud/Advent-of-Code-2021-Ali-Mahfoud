with open("/home/alimahfoud24/ALI/inputDay14.txt") as file:
    polymer_template_S = file.readline().strip(' \n ')
    line = file.readline()
    line = file.readline()
    data = dict()
    while line:
        insertion = line.strip('\n').split('->')
        data[insertion[0].strip(' ')] = insertion[1].strip(' ')
        line = file.readline()
    polymer_template = dict.fromkeys(data, 0)
    for i in range(len(polymer_template_S)-1):
        polymer_template[polymer_template_S[i:(i+2)]] += 1

for steps in range(10):
    n = dict.fromkeys(polymer_template, 0)
    for i in polymer_template:
        n[i[0]+data[i]] += polymer_template[i]
        n[data[i]+i[1]] += polymer_template[i]
    polymer_template = n


ele = dict.fromkeys(data.values(), 0)
for x in polymer_template:
    ele[x[0]] += polymer_template[x]
    ele[x[1]] += polymer_template[x]
for y in ele:
    if ele[y] % 2 == 1:
        ele[y] = (ele[y]//2)+1
    else:
        ele[y] = (ele[y]//2)

Occur_max = ele[max(ele, key=ele.get)]
Occur_min = ele[min(ele, key=ele.get)]
Result = Occur_max-Occur_min

print('After 10 steps, taking the quantity of the most common element and subtract the quantity of the least common element we get: ', Result)
