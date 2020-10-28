import sys

def generate_diamond(letter):
    if letter.upper() not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print("Please provide valid letter.")
        return
    result = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    width_and_height = calculate_width_and_height(alphabet.index(letter.upper()))
    spaces = int((width_and_height - 1) / 2)
    index = 0
    switch = False
    for line in range(width_and_height):
        str = ""
        for _ in range(spaces):
            str = str + " "
        if line == 0 or line == width_and_height - 1:
            str = str + alphabet[index]
        else:
            str = str + alphabet[index]
            for _ in range(calculate_middle_space(width_and_height, spaces)):
                str = str + " "
            str = str + alphabet[index]
        for _ in range(spaces):
            str = str + " "
        if switch is False:
            spaces = spaces - 1
            index = index + 1
        else:
            spaces = spaces + 1
            index = index - 1
        if spaces == 0:
            switch = True
        result.append(str)
    for i in result:
        print(i)

def calculate_width_and_height(index):
    return index * 2 + 1

def calculate_middle_space(width_and_height, spaces):
    return width_and_height - (spaces * 2) - 2


if __name__ == "__main__":
    generate_diamond(str(sys.argv[1]))