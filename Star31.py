with open("/home/alimahfoud24/ALI/inputDay16.txt") as file:
    data = file.readline().strip('\n').splitlines()
hex_length = 16
transmission_code = bin(int(data[0], hex_length))[2:]
transmission_len = len(transmission_code)
Result = 0
index = 0
while index < transmission_len and '1' in transmission_code[index:]:
    num = int(transmission_code[index: index + 3], 2)
    type_ID = int(transmission_code[index+3: index + 6], 2)
    index += 6
    Result += num
    if type_ID == 4:
        x = ''
        while transmission_code[index] != '0':
            x += transmission_code[index + 1: index + 5]
            index += 5
        x += transmission_code[index + 1: index + 5]
        index += 5
        x = int(x, 2)
    else:
        length_type_ID = int(transmission_code[index], 2)
        index += 1
        if length_type_ID == 0:
            x = int(transmission_code[index: index + 15], 2)
            index += 15
        elif length_type_ID == 1:
            x = int(transmission_code[index: index + 11], 2)
            index += 11
print('After adding up the version numbers in all packets, we get: ', Result)
