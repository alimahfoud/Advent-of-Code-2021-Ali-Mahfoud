data = []
with open("/home/alimahfoud24/ALI/inputDay20.txt") as file:
    line = file.readline()
    while line:
        data.append(line.strip('\n'))
        line = file.readline()

image = set()

for x in range(len(data[2:])):
    for y in range(len(data[2:][0])):
        if data[2:][x][y] == "#":
            image.add((x, y))


def enhance(image, x_min, x_max, y_min, y_max):
    enhanced_image = set()
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            p = ""
            for x2 in range(-1, 2):
                for y2 in range(-1, 2):
                    p += "1" if (x + x2, y + y2) in image else "0"
            if data[0][int(p, 2)] == "#":
                enhanced_image.add((x, y))
    return enhanced_image


x_min = min(x for x, _ in image) - 100
x_max = max(x for x, _ in image) + 100
y_min = min(y for _, y in image) - 100
y_max = max(y for _, y in image) + 100

for i in range(2):
    x_min += 1
    x_max -= 1
    y_min += 1
    y_max -= 1
    image = enhance(image, x_min, x_max, y_min, y_max)

Result = len(image)
print('After enhancing the image 2 times, there are:',
      Result, 'lit pixels in the resulting image.')
