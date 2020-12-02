import sys

class Node:
    def __init__(self, data_value=None):
        self.data_value = data_value
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
            if pointer.data_value > i.data_value:
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


if __name__ == "__main__":
    build_binary_tree([6, 3, 8, 1, 9, 7, 2, 4, 0])
    #build_binary_tree(str(sys.argv[1]))