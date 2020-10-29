import sys

def calculate_change(input, coins):
    if input <= 0:
        return "Input cannot be equal or less to 0."
    if input < coins[0]:
        return "Input cannot be less to the smallest coin."
    result = []
    coins_tmp = coins
    for _ in reversed(coins):
        result_tmp = []
        input_tmp = input
        for c in reversed(coins_tmp):
            while input_tmp >= c:
                result_tmp.append(c)
                input_tmp = input_tmp - c
        result.append(result_tmp)
        coins_tmp = coins_tmp[:-1]

    final = result[0]
    for r in result:
        if len(r) < len(final):
            final = r

    # for i in result:
    #     for j in result:
    #         if len(i) > len(j):
    #             tmp = result[result.index(j)]
    #             result[result.index(j)] = result[result.index(i)]
    #             result[result.index(i)] = tmp

    print(final)
    return final


if __name__ == "__main__":
    calculate_change(int(sys.argv[1]), list(map(int, sys.argv[2].strip('[]').split(','))))