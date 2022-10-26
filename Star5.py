with open("/home/alimahfoud24/ALI/inputDay3.txt", 'r') as file:
    row = file.readlines()
    code = [value.strip() for value in row]

    gamma = ''
    epsilon = ''

for i in range(len(code[0])):
    allvalues = [value[i] for value in code]
    if allvalues.count('0') > len(code)/2:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
print(gamma)
print("Gamma is: ", gamma, " in binary and ", int(gamma, 2), " in decimal")
print("Epsilon is: ", epsilon, " in binary and ", int(epsilon, 2), " in decimal")
print("The Power Consumption of the Submarine: ", int(gamma, 2)*int(epsilon, 2))
