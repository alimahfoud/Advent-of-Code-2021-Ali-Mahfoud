with open("/home/alimahfoud24/ALI/inputDay8.txt") as file:
    data = [row for row in file.read().strip().split('\n')]
    inputs = [row.split('|')[0].strip().split(' ') for row in data]
    outputs = [row.split('|')[1].strip().split(' ') for row in data]
appearances = 0

for i in range(len(data)):
    data_dic = {}
    for value in inputs[i]:
        if len(value) == 2:
            data_dic[1] = value
        elif len(value) == 4:
            data_dic[4] = value
        elif len(value) == 3:
            data_dic[7] = value
        elif len(value) == 7:
            data_dic[8] = value

    for value in inputs[i]:
        if len(value) == 6:
            if set(data_dic[4]).issubset(set(value)):
                data_dic[9] = value
            elif set(data_dic[1]).issubset(set(value)):
                data_dic[0] = value
            else:
                data_dic[6] = value

    for value in inputs[i]:
        if len(value) == 5:
            if set(value).issubset(set(data_dic[6])):
                data_dic[5] = value
            elif set(data_dic[1]).issubset(set(value)):
                data_dic[3] = value
            else:
                data_dic[2] = value

    num = []
    for value in outputs[i]:
        for t, v in data_dic.items():
            if set(value) == set(v):
                num.append(str(t))

    num = int(''.join(num))
    appearances += num

print('After adding up all of the output values, we get: ', appearances,)
