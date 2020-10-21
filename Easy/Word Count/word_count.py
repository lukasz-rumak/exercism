import sys
from collections import OrderedDict

def count_words(input):
    words = []
    tmp = ""
    while input[len(input) - 1] == " ":
        input = input[:-1]
    input = input + " "
    for i in input:
        if i == "," or i == "." or i == "?" or i == "!":
            continue
        if i != " ":
            tmp = tmp + i
        else:
            if tmp != "":
                words.append(tmp.lower())
            tmp = ""

    result = {}
    for w in words:
        count = 0
        for i in words:
            if w == i:
                count = count + 1
        result.update({w: count})

    print(result)

if __name__ == "__main__":
    count_words(str(sys.argv[1]))