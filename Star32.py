from functools import reduce
with open("/home/alimahfoud24/ALI/inputDay16.txt") as file:
    data = file.readline().strip('\n').splitlines()
hex_length = 16
transmission_code = bin(int(data[0], hex_length))[2:]
transmission_len = len(transmission_code)

packet = []
function_list = {
    0: sum,
    1: lambda x: reduce(lambda i, j: i * j, x),
    2: min,
    3: max,
    5: lambda x: int(x[0] > x[1]),
    6: lambda x: int(x[0] < x[1]),
    7: lambda x: int(x[0] == x[1])
}


def solve(code):
    if packet[code][1] == 4:
        return packet[code][2]
    Result = []
    for i in sol_stack[code]:
        Result.append(solve(i))
    return function_list[packet[code][1]](Result)


index = 0
while index < transmission_len and '1' in transmission_code[index:]:
    num = int(transmission_code[index: index + 3], 2)
    type_ID = int(transmission_code[index+3: index + 6], 2)
    index += 6
    if type_ID == 4:
        x = ''
        while transmission_code[index] != '0':
            x += transmission_code[index + 1: index + 5]
            index += 5
        x += transmission_code[index + 1: index + 5]
        index += 5
        x = int(x, 2)
        packet.append([num, type_ID, x, index])
    else:
        length_type_ID = int(transmission_code[index], 2)
        index += 1
        if length_type_ID == 0:
            x = int(transmission_code[index: index + 15], 2)
            index += 15
        elif length_type_ID == 1:
            x = int(transmission_code[index: index + 11], 2)
            index += 11
        packet.append([num, type_ID, length_type_ID, x, index])

stack = []
sol_stack = [[] for _ in range(len(packet))]
en_packet = enumerate(packet)
for i, j in en_packet:
    if len(stack) > 0:
        ss = stack[-1]
        sol_stack[ss].append(i)
        packet[ss][3] -= 1
        if packet[ss][3] == 0:
            stack.pop()
    while len(stack) > 0:
        ss = stack[-1]
        if packet[ss][2] == 0 and packet[ss][3] <= j[-1] - packet[ss][-1]:
            stack.pop()
        else:
            break
    if j[1] != 4:
        stack.append(i)

print('After evaluating the expression represented by the hexadecimal-encoded BITS transmission, we get: ', solve(0))
