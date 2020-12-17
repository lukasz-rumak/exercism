import sys
import random


class Node:

    def __init__(self, value=None):
        self.value = value
        self.next_value_left = None
        self.next_value_right = None


class BuildBinaryTree:

    def __init__(self, array):
        self.array = array

    def build_binary_tree(self):
        tree = Node(self.array[0])
        tree_array = []
        for i in self.array:
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


class SortTree:

    def __init__(self, tree_to_read):
        self.tree_to_read = tree_to_read

    def read_tree_in_order(self):
        sorted_array = []
        tmp_array = [self.tree_to_read]
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


class FindNumberInTree:

    def __init__(self, number, tree):
        self.number = number
        self.tree = tree

    def find_number(self):
        pointer = self.tree
        while True:
            if self.number == pointer.value:
                return True
            elif self.number > pointer.value:
                if pointer.next_value_right is not None:
                    pointer = pointer.next_value_right
                else:
                    return False
            else:
                if pointer.next_value_left is not None:
                    pointer = pointer.next_value_left
                else:
                    return False


if __name__ == "__main__":
    BuildBinaryTree(str(sys.argv[1])).build_binary_tree()