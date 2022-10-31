import heapq
data = []
with open("/home/alimahfoud24/ALI/inputDay15.txt") as file:
    line = file.readline()
    while line:
        data.append(line.strip('\n'))
        line = file.readline()
risk_level_map = [list(map(int, x)) for x in data]
RLM_length = len(risk_level_map)
Table_length = 5*RLM_length
path_table = [[0]*Table_length for _ in range(Table_length)]

for i in range(Table_length):
    for j in range(Table_length):
        path_table[i][j] = (risk_level_map[i % RLM_length][j %
                            RLM_length]+(i//RLM_length)+(j//RLM_length)-1) % 9+1

priority_queue = [(0, 0, 0)]
visited_path = set()

while priority_queue:
    risk_level, x, y = heapq.heappop(priority_queue)
    if x == y == RLM_length - 1:
        print('The lowest total risk of any path from the top left to the bottom right is: ', risk_level)
        break
    if (x, y) in visited_path:
        continue
    visited_path.add((x, y))
    for next_x, next_y in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if next_x < 0 or next_y < 0 or next_y >= RLM_length or next_x >= RLM_length:
            continue
        if (next_x, next_y) in visited_path:
            continue
        heapq.heappush(priority_queue, (risk_level +
                       path_table[next_x][next_y], next_x, next_y))
