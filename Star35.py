data_assignment = []
file = open("/home/alimahfoud24/ALI/inputDay18.txt")


def get_data(i):
    if isinstance(i, int):
        return [i]
    else:
        return [get_data(j) for j in i]


for line in file:
    data_assignment.append(get_data(eval(line)))


def r_addition(i, j):
    if i is None:
        return
    if len(i) == 1:
        i[0] += j
    else:
        r_addition(i[1], j)


def l_addition(i, j):
    if i is None:
        return
    if len(i) == 1:
        i[0] += j
    else:
        l_addition(i[0], j)


def explode(value, left=None, right=None, depth=0):
    if len(value) == 1:
        return False
    if depth >= 4 and len(value[0]) == len(value[1]) == 1:
        r_addition(left, value[0][0])
        l_addition(right, value[1][0])
        value[:] = [0]
        return True
    else:
        return explode(value[0], left, value[1], depth+1) or explode(value[1], value[0], right, depth + 1)


def split(i):
    if len(i) == 1:
        if i[0] >= 10:
            i[:] = [[i[0]//2], [i[0]-i[0]//2]]
            return True
        else:
            return False
    else:
        return split(i[0]) or split(i[1])


def reduce(i):
    while explode(i) or split(i):
        pass


def mag(i):
    if len(i) == 1:
        return i[0]
    else:
        return 3*mag(i[0])+2*mag(i[1])


a = data_assignment[0]

for i in data_assignment[1:]:
    a = [a, i]
    reduce(a)

print(mag(a))
