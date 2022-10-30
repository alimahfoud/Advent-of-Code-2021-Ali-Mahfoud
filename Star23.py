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
    if p[-1] != 'end':
        for n in Path[p[-1]]:
            if (n not in p) or (n.upper() == n):
                p.append(n)
                get_path()
                p.pop()
    else:
        Result.append(p)


p = ['start']
Result = []
get_path()
print('Through this cave system, there are: ', len(Result),
      ' paths that visit small caves at most once.')
