import sys


def quicksort(array_to_sort):
    array_sorted = []
    for _ in range(len(array_to_sort)):
        array_sorted.append(0)
    array = array_to_sort
    sum_array_to_sort = sum(array_to_sort)
    sum_array_sorted = 0
    while sum_array_sorted != sum_array_to_sort:
        array, j = do_quicksort(array)
        array_sorted[j] = array[j]

        sum_array_sorted = sum_array_sorted + array[j]

    return array_sorted


def do_quicksort(array):
    pivot = array[-1]
    j = 0
    for i in range(len(array)):
        if array[i] <= pivot:
            tmp = array[j]
            array[j] = array[i]
            array[i] = tmp
            j = j + 1
    return array, j - 1


if __name__ == "__main__":
    quicksort([3,9,4,6,7,1,2,8,5])
    #quicksort(str(sys.argv[1]))