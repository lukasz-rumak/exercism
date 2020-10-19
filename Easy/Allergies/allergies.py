import sys

def return_allergies(input):
    if input <= 0 or input > 255:
        print("Please provide valid input.")
        return
    data = {
        1: "eggs",
        2: "peanuts",
        4: "shellfish",
        8: "strawberries",
        16: "tomatoes",
        32: "chocolate",
        64: "pollen",
        128: "cats",
    }
    result = []
    for k, v in reversed(data.items()):
        if input >= k:
            input = input - k
            result.append(v)
    print(result)

if __name__ == "__main__":
    return_allergies(int(sys.argv[1]))

