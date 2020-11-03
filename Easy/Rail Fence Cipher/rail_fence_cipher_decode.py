import sys


def rail_fence_cipher_decode(sentence, rails):
    if rails == 1:
        return "Rails cannot be 1"
    length = calculate_length(rails)
    sentence_length = len(sentence)
    result = []
    index = 0
    switch = False
    for _ in range(length):
        result.append(0)

    for _ in range(length):
        tmp_length = index
        while tmp_length < sentence_length:
            result[index] = result[index] + 1
            tmp_length = tmp_length + length
        index = index + 1

    result_s = []
    for _ in sentence:
        result_s.append("")

    index = 0
    counter = 0
    for s in sentence:
        tmp_length = 0
        while result[index] > 0:
            result_s[counter + tmp_length] = s
            tmp_length = tmp_length + length
            result[index] = result[index] - 1
        index = index + 1
        if switch:
            counter = counter - 1
        else:
            counter = counter + 1
        if counter == rails - 1:
            switch = True

    final = ""
    for r in result:
        final = final + r
    return final

def calculate_length(rails):
    return (rails - 2) * 2 + 2

if __name__ == "__main__":
    rail_fence_cipher_decode("LKIUAJIMKMEKAAUSSDSRTORZBY", 6)
    # rail_fence_cipher_decode(str(sys.argv[1]), int(sys.argv[2]))
