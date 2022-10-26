with open("/home/alimahfoud24/ALI/inputDay3.txt", 'r') as file:
    row = file.readlines()
    code = [value.strip() for value in row]

from copy import copy
oxygen_list = copy(code)

for i in range(len(code[0])):
    if len(oxygen_list) == 1:
        break
    allvalues = [value[i] for value in oxygen_list]
    oxybit = '1' if allvalues.count('1') >= len(oxygen_list)/2 else '0'
    oxygen_list = [value for value in oxygen_list if value[i] == oxybit]
    oxygen_generator_rating = int(oxygen_list[0], 2)
print("Oxygen value: ",
      oxygen_list[0], " in binary and ", oxygen_generator_rating, " in decimal")

CO2_list = copy(code)

for i in range(len(code[0])):
    if len(CO2_list) == 1:
        break
    allvalues = [value[i] for value in CO2_list]
    CO2bit = '0' if allvalues.count('1') >= len(CO2_list)/2 else '1'
    CO2_list = [value for value in CO2_list if value[i] == CO2bit]
    CO2_scrubber_rating = int(CO2_list[0], 2)
print("CO2 value: ", CO2_list[0], " in binary and ",
      CO2_scrubber_rating, " in decimal")

print("The life supporting rate of the submarine is: ",
      oxygen_generator_rating*CO2_scrubber_rating)
