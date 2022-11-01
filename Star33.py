with open("/home/alimahfoud24/ALI/inputDay17.txt") as file:
    data = [file.readline().split()]
data = data[0][2:]
data_x, data_y = data[0][2:-1], data[1][2:]
x1, x2 = data_x.split('..')
y1, y2 = data_y.split('..')
x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
target_max = 2*abs(y1)+1
highest_point = 0
for y in range(y1, abs(y1)):
    for x in range(1, x2+1):
        x_v, y_v = x, y
        xprob = yprob = ymax = 0
        for i in range(target_max+1):
            xprob += x_v
            yprob += y_v
            x_v = max((x_v - 1), 0)
            y_v -= 1
            ymax = max(ymax, yprob)
            if x1 <= xprob <= x2 and y1 <= yprob <= y2:
                highest_point = max(highest_point, ymax)
                break
            elif xprob > x2 or yprob < y1:
                break

print('The highest y position the probe to reach on this trajectory is: ', highest_point)
