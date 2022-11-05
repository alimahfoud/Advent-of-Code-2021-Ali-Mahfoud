Scanners = []
Coordinations = set()
with open("/home/alimahfoud24/ALI/inputDay19.txt") as file:
    for line in file:
        if line.strip() == "":
            continue
        if 'scanner' in line:
            if len(Coordinations) > 0:
                Scanners.append(Coordinations)
            Coordinations = set()
            continue
        else:
            x, y, z = (int(i) for i in line.split(',') if i != "")
            Coordinations.add((x, y, z))
    Scanners.append(Coordinations)

Scanner_Beacons_Range = 1000
Common_Beacons = 12
Rotation_Axis = [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1), (1, 2, -3), (1, -3, 2), (2, 1, -3), (2, -3, 1), (-3, 1, 2), (-3, 2, 1), (1, -2, 3), (1, 3, -2), (-2, 1, 3), (-2, 3, 1), (3, 1, -2), (3, -2, 1), (1, -2, -3), (1, -3, -2), (-2, 1, -3), (-2, -3, 1), (-3, 1, -2), (-3, -2, 1), (-1, 2, 3),
                 (-1, 3, 2), (2, -1, 3), (2, 3, -1), (3, -1, 2), (3, 2, -1), (-1, 2, -3), (-1, -3, 2), (2, -1, -3), (2, -3, -1), (-3, -1, 2), (-3, 2, -1), (-1, -2, 3), (-1, 3, -2), (-2, -1, 3), (-2, 3, -1), (3, -1, -2), (3, -2, -1), (-1, -2, -3), (-1, -3, -2), (-2, -1, -3), (-2, -3, -1), (-3, -1, -2), (-3, -2, -1)]


def update_position(input_xyz: tuple, Axis_rotation, offset):
    output_coordinates = [0, 0, 0]
    for i in range(len(output_coordinates)):
        output_coordinates[abs(Axis_rotation[i]) - 1] = input_xyz[i]
        if Axis_rotation[i] < 0:
            output_coordinates[abs(Axis_rotation[i]) - 1] *= -1
    for i, j in enumerate(offset):
        output_coordinates[i] += j
    return tuple(output_coordinates)


def update_position2(starting_position, finising_position):
    for rotation in Rotation_Axis:
        no_offset = update_position(starting_position, rotation, (0, 0, 0))
        offset = tuple(i - j for j, i in zip(no_offset, finising_position))
        yield rotation, offset


def check_update(xyz1, xyz2, Rotation, new_position):
    matches = 0
    for xyz in xyz1:
        if update_position(xyz, Rotation, new_position) in xyz2:
            matches += 1
            if matches == Common_Beacons:
                return True
    return False


def ref_points(xyz, range=100):
    common_num = {}
    limit = Scanner_Beacons_Range - range
    for x, y, z in xyz:
        if abs(x) > limit or abs(y) > limit or abs(z) > limit:
            continue
        for xx, yy, zz in xyz:
            if abs(x - xx) == 0 or abs(y - yy) == 0 or abs(z - zz) == 0:
                continue
            if abs(x - xx) < range and abs(y - yy) < range and abs(z - zz) < range:
                common_num[(x, y, z)] = common_num.get(
                    (x, y, z), 0) + ((abs(x - xx) + 1) * (abs(y - yy) + 1) * (abs(z - zz) + 1))
    return common_num


def common_beacon(xyz1, xyz2, reference):
    reference_n = ref_points(xyz2)
    for i, j in reference.items():
        for k, l in reference_n.items():
            if l != j:
                continue
            for Rotation, new_position in update_position2(k, i):
                if check_update(xyz2, xyz1, Rotation, new_position):
                    return Rotation, new_position


def combine_coordinates(Scanners):
    xyz_abs = Scanners[0]
    ref_abs = ref_points(Scanners[0])
    all_detected = set()
    offset = [None] * len(Scanners)
    offset[0] = (0, 0, 0)
    while True:
        detected = set()
        for i, j in enumerate(Scanners[1:]):
            if (i + 1) in all_detected:
                continue
            k = common_beacon(xyz_abs, j, ref_abs)
            if k is not None:
                offset[i + 1] = k[1]
                detected.add(i + 1)
                all_detected.add(i + 1)
                for jj in j:
                    updated = update_position(jj, k[0], k[1])
                    xyz_abs.add(updated)
                    for l, m in ref_points(j).items():
                        ref_abs[update_position(l, k[0], k[1])] = m
        if len(detected) == 0:
            break
    return xyz_abs, offset


xyz = combine_coordinates(Scanners)[1]
largest_Manhatan_distance = 0
for x, y, z in xyz:
    for x1, y1, z1 in xyz:
        if (abs(x-x1) + abs(y-y1) + abs(z-z1)) > largest_Manhatan_distance:
            largest_Manhatan_distance = (abs(x-x1) + abs(y-y1) + abs(z-z1))

print('The largest Manhattan distance between any two scanners is:',
      largest_Manhatan_distance)
