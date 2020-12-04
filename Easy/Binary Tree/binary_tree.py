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


class GenerateRandomArray:

    def __init__(self, from_number, to_number, array_length):
        self.from_number = from_number
        self.to_number = to_number
        self.array_length = array_length

    def generate_random_array_with_int(self):
        return random.sample(range(self.from_number, self.to_number), self.array_length)


class TestTree:

    def __init__(self, random_array, tree_array_sorted):
        self.random_array = random_array
        self.tree_array_sorted = tree_array_sorted

    def test_tree_array_sorted(self):
        self.random_array.sort()
        counter = 0
        for _ in range(len(self.random_array)):
            if self.random_array[counter] != self.tree_array_sorted[counter]:
                return False
            counter = counter + 1
        return True


if __name__ == "__main__":
    random_array = GenerateRandomArray(-30, 30, 30).generate_random_array_with_int()
    binary_tree = BuildBinaryTree(random_array).build_binary_tree() #[6, 3, 8, 1, 9, 7, 2, 4, 0, 17, -14, -22, -8, -4, -9, 11]
    tree_array_sorted = SortTree(binary_tree).read_tree_in_order()
    result = TestTree(random_array, tree_array_sorted).test_tree_array_sorted()
    str = "123"
    #build_binary_tree(str(sys.argv[1]))

    # if number is present in tree?
    # sort the tree