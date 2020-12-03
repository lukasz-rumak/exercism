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


def read_tree_in_order(tree_to_read):
    sorted_array = []
    tmp_array = [tree_to_read]
    while len(tmp_array) > 0:
        if tmp_array[-1].next_value_left is None:
            sorted_array.append(tmp_array[-1].value)
            if len(tmp_array) > 1:
                tmp_array[-2].next_value_left = None
            if tmp_array[-1].next_value_right is not None:
                tmp = tmp_array[-1].next_value_right
                tmp_array = tmp_array[:-1]
                tmp_array.append(tmp)
            else:
                tmp_array = tmp_array[:-1]
        else:
            tmp_array.append(tmp_array[-1].next_value_left)
    return sorted_array


if __name__ == "__main__":
    binary_tree = build_binary_tree([6, 3, 8, 1, 9, 7, 2, 4, 0, 17, -14, -22, -8, -4, -9, 11])
    result = read_tree_in_order(binary_tree)
    str = "123"
    #build_binary_tree(str(sys.argv[1]))