lanternfish_data = {}
with open("/home/alimahfoud24/ALI/inputDay6.txt") as file:
    Array = [int(x) for x in file.readline().split(',')]
    for x in range(max(9, max(Array))):
        lanternfish_data[x] = 0
    for y in Array:
        lanternfish_data[y] += 1

Number_of_days = 256

for Days in range(Number_of_days):
    Zeroes_data = lanternfish_data[0]
    lanternfish_data[0] = 0
    for i in range(1, len(lanternfish_data)):
        lanternfish_data[i-1] += lanternfish_data[i]
        lanternfish_data[i] = 0
    lanternfish_data[6] += Zeroes_data
    lanternfish_data[8] += Zeroes_data


Number_of_landernfish = 0
for j in lanternfish_data:
    Number_of_landernfish += lanternfish_data[j]

print('After ', Number_of_days, ' days, there would be: ', Number_of_landernfish)
