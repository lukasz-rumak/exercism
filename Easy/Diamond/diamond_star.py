import sys

def generate_diamond(width_and_height):
    if width_and_height % 2 == 0:
        print("Please provide an odd number!")
        return
    result = []
    spaces = int((width_and_height - 1) / 2)
    switch = False
    for line in range(width_and_height):
        str = ""
        for _ in range(spaces):
            str = str + " "
        if line == 0 or line == width_and_height - 1:
            str = str + "*"
        else:
            str = str + "*"
            for _ in range(calculate_middle_space(width_and_height, spaces)):
                str = str + " "
            str = str + "*"
        for _ in range(spaces):
            str = str + " "
        if switch is False:
            spaces = spaces - 1
        else:
            spaces = spaces + 1
        if spaces == 0:
            switch = True
        result.append(str)
    for i in result:
        print(i)

def calculate_middle_space(width_and_height, spaces):
    return width_and_height - (spaces * 2) - 2

if __name__ == "__main__":
    generate_diamond(int(sys.argv[1]))
