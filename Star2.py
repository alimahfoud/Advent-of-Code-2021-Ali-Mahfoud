import csv

with open("/home/alimahfoud24/ALI/inputDay1.csv", 'r') as data_file:
    csvreader = csv.reader(data_file)
    count_increased = 0
    Depth_Measurement = []
    for row in csvreader:
        Depth_Measurement.append(row[0])

Depth_Measurement_num = list(map(int, Depth_Measurement))

first_measurement = 0
second_measurement = 1
third_measurement = 2
fourth_measurement = 3
A = Depth_Measurement_num[first_measurement] + \
    Depth_Measurement_num[second_measurement] + \
    Depth_Measurement_num[third_measurement]
B = Depth_Measurement_num[second_measurement] + \
    Depth_Measurement_num[third_measurement] + \
    Depth_Measurement_num[fourth_measurement]
for i in Depth_Measurement_num:
    if (fourth_measurement == len(Depth_Measurement_num)):
        break
    elif A < B:
        count_increased += 1

    A = Depth_Measurement_num[first_measurement] + \
        Depth_Measurement_num[second_measurement] + \
        Depth_Measurement_num[third_measurement]
    B = Depth_Measurement_num[second_measurement] + \
        Depth_Measurement_num[third_measurement] + \
        Depth_Measurement_num[fourth_measurement]
    first_measurement += 1
    second_measurement += 1
    third_measurement += 1
    fourth_measurement += 1
print("Number of three_measurements sums larger than previous three_measurements sums: ", count_increased)
