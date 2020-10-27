import sys

def generate_diamond(width_and_height):
    result = []
    empty_space = int((width_and_height - 1) / 2)
    switch = False
    for line in range(width_and_height):
        str = ""
        for _ in range(empty_space):
            str = str + " "
        if line == 0 or line == width_and_height - 1:
            str = str + "*"
        else:
            str = str + "*"
            for _ in range(calculate_middle_space(width_and_height, empty_space)):
                str = str + " "
            str = str + "*"
        for _ in range(empty_space):
            str = str + " "
        if switch is False:
            empty_space = empty_space - 1
        else:
            empty_space = empty_space + 1
        if empty_space == 0:
            switch = True
        result.append(str)
    for i in result:
        print(i)

def calculate_middle_space(width_and_height, empty_space):
    return width_and_height - (empty_space * 2) - 2

if __name__ == "__main__":
    generate_diamond(int(sys.argv[1]))
