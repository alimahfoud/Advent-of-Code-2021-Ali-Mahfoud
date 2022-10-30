Path = dict()
with open("/home/alimahfoud24/ALI/inputDay12.txt") as file:
    line = file.readline()
    while line:
        destinations = [x for x in line.strip('\n').split('-')]
        if Path.get(destinations[0], ' ') == ' ':
            Path[destinations[0]] = []
        if Path.get(destinations[1], ' ') == ' ':
            Path[destinations[1]] = []
        Path[destinations[0]].append(destinations[1])
        Path[destinations[1]].append(destinations[0])
        line = file.readline()



def get_path():
    global Result
    if p[-1] != 'end':
        for n in Path[p[-1]]:
            if (n != 'start') and OneCaveTwice(p) and ((n.upper() == n) or OncePerCave(p)):
                p.append(n)
                get_path()
                p.pop()
    elif OneCaveTwice(p):
        Result += 1


def OneCaveTwice(cave_l):
    lower_cave = [x for x in cave_l if x.lower() == x]
    return len(lower_cave)-len(set(lower_cave)) <= 1


def OncePerCave(cave_l2):
    lower_cave2 = [x for x in cave_l2 if x.count(x) < 2]
    return True


p = ['start']
Result = 0
get_path()
print('Through this cave system, there are: ', Result, ' paths.')
