import csv

with open("/home/alimahfoud24/ALI/inputDay1.csv", 'r') as data_file:
    csvreader = csv.reader(data_file)
    count_increased = 0
    Depth_Measurement = []
    for row in csvreader:
        Depth_Measurement.append(row[0])

Depth_Measurement_num = list(map(int, Depth_Measurement))

measurement = 0
next_measurement = 1

for i in Depth_Measurement_num:
    if next_measurement == len(Depth_Measurement_num):
        break
    elif Depth_Measurement_num[measurement] < Depth_Measurement_num[next_measurement]:
        count_increased += 1
    measurement += 1
    next_measurement += 1
print("Number of measurements largest than previous measurements: ",
      count_increased)
