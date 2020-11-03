import sys


def rail_fence_cipher_encode(sentence, rails):
    if rails == 1:
        return "Rails cannot be 1"
    sentence_parsed = ""
    for s in sentence:
        if s in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            sentence_parsed = sentence_parsed + s
    result = []
    for _ in range(rails):
        result.append("")
    index = 0
    index_switch = False
    for s in sentence_parsed:
        result[index] = result[index] + s
        if index_switch:
            index = index - 1
        else:
            index = index + 1
        if index == rails:
            index_switch = True
            index = index - 2
        if index == 0:
            index_switch = False

    final = ""
    for r in result:
        final = final + r
    return final


if __name__ == "__main__":
    rail_fence_cipher_encode(str(sys.argv[1]), int(sys.argv[2]))
