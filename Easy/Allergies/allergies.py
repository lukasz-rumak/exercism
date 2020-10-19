import sys

def return_allergies(input):
    if input <= 0:
        print("Please provide valid input.")
        return
    result = []
    variable = 256
    variables = []
    if input > 255:
        while variable <= input:
            variables.append(variable)
            variable = variable * 2
    for v in reversed(variables):
        print(input)
        print(v)
        if input >= v:
            input = input - v
            result.append("Unknown")
        if input < variables[0]:
            break

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
    for k, v in reversed(data.items()):
        if input >= k:
            input = input - k
            result.append(v)
    print(result)

if __name__ == "__main__":
    return_allergies(int(sys.argv[1]))

