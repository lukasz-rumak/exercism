import sys


def quicksort(array_to_sort):
    array = array_to_sort
    array = do_quicksort(array, 0, len(array) - 1)
    #print("Sorted array:", array)
    return array


def do_quicksort(array, index_start, index_end):
    #print("------")
    #print(array)
    #print(index_start, index_end)
    if index_start >= index_end:
        return array
    else:
        pivot = array[index_end]
        j = index_start
        for i in range(index_start, index_end + 1):
            if array[i] <= pivot:
                tmp = array[j]
                array[j] = array[i]
                array[i] = tmp
                j = j + 1
        array = do_quicksort(array, index_start, j - 2)
        array = do_quicksort(array, j, index_end)
        return array


if __name__ == "__main__":
    quicksort([12, 16, 9, 4, -22, 6, 23, 7, -15, 1, 9, 8, 4, 11, 5])
    #quicksort(str(sys.argv[1]))