import sys


def quicksort(array_to_sort):
    array = array_to_sort
    array = do_quicksort(array, 0, len(array) - 1)
    return array


def do_quicksort(array, index_start, index_end):
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


def do_quicksort_clean(array):
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