import sys


def rail_fence_cipher_decode(sentence, rails):
    if rails == 1:
        return "Rails cannot be 1"
    length = calculate_length(rails)
    sentence_length = len(sentence)
    result = []
    index = 0

    for _ in range(length):
        result.append(0)
    for _ in range(length):
        tmp_length = index
        while tmp_length < sentence_length:
            result[index] = result[index] + 1
            tmp_length = tmp_length + length
        index = index + 1

    result_merged = []
    for _ in range(rails):
        result_merged.append(0)

    index = 0
    for _ in result_merged:
        if index == 0:
            result_merged[index] = result[index]
        elif index == rails - 1:
            result_merged[index] = result[rails - 1]
        else:
            result_merged[index] = result[index] + result[length - index]
        index = index + 1

    result_str = []
    for _ in range(rails):
        result_str.append([])
    index = 0
    counter = 0
    for s in sentence:
        if counter < result_merged[index]:
            result_str[index].append(s)
            counter = counter + 1
        else:
            index = index + 1
            counter = 0
            result_str[index].append(s)
            counter = counter + 1

    final = ""
    index = 0
    index_switch = False
    for _ in range(len(sentence)):
        final = final + result_str[index][0]
        result_str[index] = result_str[index][1:]  # delete first element from the list
        if index_switch:
            index = index - 1
        else:
            index = index + 1
        if index == rails:
            index_switch = True
            index = index - 2
        if index == 0:
            index_switch = False

    return final


def calculate_length(rails):
    return (rails - 2) * 2 + 2


if __name__ == "__main__":
    rail_fence_cipher_decode("LKIUAJIMKMEKAAUSSDSRTORZBY", 6)
    # rail_fence_cipher_decode(str(sys.argv[1]), int(sys.argv[2]))