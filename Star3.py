import csv
from turtle import forward

with open("/home/alimahfoud24/ALI/inputDay2.csv", 'r') as data_file:
    csvreader = csv.reader(data_file)
    Displacement = []
    for row in csvreader:
        Displacement.append(row[0])
movement = 0
forward_total = 0
down_total = 0
up_total = 0

for i in Displacement:
    if movement > len(Displacement):
        break
    elif Displacement[movement].__contains__('forward'):
        forward_total += int((Displacement[movement])[8])
    elif Displacement[movement].__contains__('down'):
        down_total += int((Displacement[movement])[5])
    elif Displacement[movement].__contains__('up'):
        up_total += int((Displacement[movement])[3])
    movement += 1

depth_total = down_total - up_total
final_result = forward_total*depth_total
print("Total Horizantal Position: ", forward_total)
print("Total Depth: ", depth_total)
print("Final Answer: Final Horizontal Position X Final Depth: ", final_result)
