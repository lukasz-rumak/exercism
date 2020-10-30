import sys

def calculate_luhn(card_number):
    if len(card_number) != 16:
        return "Please provide valid card number."
    result = []
    for c in card_number:
        try:
            int(c)
        except ValueError:
            return "Please provide valid card number."
        result.append(int(c))
    counter = 0
    for c in result:
        if counter == 0 or counter % 2 == 0:
            tmp = c * 2
            if tmp >= 10:
                tmp = tmp - 9
            result[counter] = tmp
        counter = counter + 1

    if sum(result) % 10 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    calculate_luhn(str(sys.argv[1]))