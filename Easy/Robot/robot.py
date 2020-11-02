import sys


def move_robot(instruction):
    coordinates = [0, 0]
    direction = [0, 1, 2, 3]  # 0 - north, 1 - east, 2 - south, 3 - west
    d = direction[0]
    for i in instruction:
        if i == "A":
            if d == 0:
                coordinates[1] = coordinates[1] + 1
            if d == 2:
                coordinates[1] = coordinates[1] - 1
            if d == 1:
                coordinates[0] = coordinates[0] + 1
            if d == 3:
                coordinates[0] = coordinates[0] - 1
        if i == "R":
            if d == 3:
                d = direction[0]
            else:
                d = direction[d + 1]
        if i == "L":
            if d == 0:
                d = direction[3]
            else:
                d = direction[d - 1]

    print(d)
    print(coordinates)


if __name__ == "__main__":
    move_robot(str(sys.argv[1]))
