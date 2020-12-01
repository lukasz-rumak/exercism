import sys


def binary_search(array, value):
    start = 0
    mid = int((len(array) - 1) / 2)
    end = len(array) - 1
    if array[start] == value:
        return start
    if array[end] == value:
        return end
    for _ in range(len(array) - 1):
        if array[int(mid)] == value:
            return int(mid)
        if array[int(mid)] > value:
            end = mid
        else:
            start = mid
        mid = int(start + ((end - start) / 2))
        if mid == start or mid == end:
            return None
    return None


if __name__ == "__main__":
    binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], 19)
    #binary_search(str(sys.argv[1]))