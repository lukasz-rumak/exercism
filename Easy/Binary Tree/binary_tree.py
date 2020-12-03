import sys

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_value_left = None
        self.next_value_right = None


def build_binary_tree(array):
    tree = Node(array[0])
    tree_array = []
    for i in array:
         tree_array.append(Node(i))
    counter = 0
    for i in tree_array[1:]:
        pointer = tree
        counter = counter + 1
        for _ in range(counter):
            if pointer.value > i.value:
                if pointer.next_value_left is None:
                    pointer.next_value_left = i
                    break
                else:
                    pointer = pointer.next_value_left
            else:
                if pointer.next_value_right is None:
                    pointer.next_value_right = i
                    break
                else:
                    pointer = pointer.next_value_right
    return tree

#if number is present in tree?
#sort the tree


def read_tree_in_order(tree):
    array = [None]
    pointer = tree
    switch = True
    while switch:
        if pointer.next_value_left is not None:
            delete_pointer = pointer
            pointer = pointer.next_value_left
        if pointer.next_value_left is None:
            if array[len(array) - 1] != pointer.value:
                array.append(pointer.value)
            if pointer.next_value_right is None:
                delete_pointer.next_value_left = None
                pointer = tree #delete_pointer?
            else:
                pointer = pointer.next_value_right




    return array




if __name__ == "__main__":
    tree = build_binary_tree([6, 3, 8, 1, 9, 7, 2, 4, 0, 17, -14, -22, -8, -4, -9])
    array = read_tree_in_order(tree)
    #build_binary_tree(str(sys.argv[1]))