import unittest
import random
import binary_tree


def build_tree():
    tree = binary_tree.Node(6)
    tree.next_value_left = binary_tree.Node(2)
    tree.next_value_left.next_value_left = binary_tree.Node(-2)
    tree.next_value_left.next_value_right = binary_tree.Node(4)
    tree.next_value_right = binary_tree.Node(10)
    tree.next_value_right.next_value_left = binary_tree.Node(8)
    tree.next_value_right.next_value_right = binary_tree.Node(12)
    return tree

def compare_two_array(first_array, second_array):
        counter = 0
        for _ in range(len(first_array)):
            if first_array[counter] != second_array[counter]:
                return False
            counter = counter + 1
        return True

def generate_random_array_with_ints(from_number, to_number, array_length):
        return random.sample(range(from_number, to_number), array_length)


class BinaryTreeTestCase(unittest.TestCase):
    def test_building_binary_tree_equal(self):
        tree_mocked = build_tree()
        tree_to_test = binary_tree.BuildBinaryTree([6, 10, 2, 12, 8, 4, -2]).build_binary_tree()
        self.assertEqual(tree_to_test.value, tree_mocked.value)
        self.assertEqual(tree_to_test.next_value_left.value, tree_mocked.next_value_left.value)
        self.assertEqual(tree_to_test.next_value_left.next_value_left.value, tree_mocked.next_value_left.next_value_left.value)
        self.assertEqual(tree_to_test.next_value_left.next_value_right.value, tree_mocked.next_value_left.next_value_right.value)
        self.assertEqual(tree_to_test.next_value_right.value, tree_mocked.next_value_right.value)
        self.assertEqual(tree_to_test.next_value_right.next_value_left.value, tree_mocked.next_value_right.next_value_left.value)
        self.assertEqual(tree_to_test.next_value_right.next_value_right.value, tree_mocked.next_value_right.next_value_right.value)

    def test_building_binary_tree_not_equal(self):
        tree_mocked = build_tree()
        tree_to_test = binary_tree.BuildBinaryTree([6, 9, 3, 11, 7, 5, -1]).build_binary_tree()
        self.assertEqual(tree_to_test.value, tree_mocked.value)
        self.assertNotEqual(tree_to_test.next_value_left.value, tree_mocked.next_value_left.value)
        self.assertNotEqual(tree_to_test.next_value_left.next_value_left.value, tree_mocked.next_value_left.next_value_left.value)
        self.assertNotEqual(tree_to_test.next_value_left.next_value_right.value, tree_mocked.next_value_left.next_value_right.value)
        self.assertNotEqual(tree_to_test.next_value_right.value, tree_mocked.next_value_right.value)
        self.assertNotEqual(tree_to_test.next_value_right.next_value_left, tree_mocked.next_value_right.next_value_left.value)
        self.assertNotEqual(tree_to_test.next_value_right.next_value_right.value, tree_mocked.next_value_right.next_value_right.value)

    def test_read_binary_tree_in_order(self):
        self.assertTrue(compare_two_array(sorted([6, 3, 8, 1, 9, 7, 2, 4, 0, 17, -14, -22, -8, -4, -9, 11]), binary_tree.SortTree(binary_tree.BuildBinaryTree([6, 3, 8, 1, 9, 7, 2, 4, 0, 17, -14, -22, -8, -4, -9, 11]).build_binary_tree()).read_tree_in_order()))

    def test_read_binary_tree_in_order_using_random_array_1(self):
        random_array = generate_random_array_with_ints(-30, 30, 30)
        self.assertTrue(compare_two_array(sorted(random_array), binary_tree.SortTree(binary_tree.BuildBinaryTree(random_array).build_binary_tree()).read_tree_in_order()))

    def test_read_binary_tree_in_order_using_random_array_2(self):
        random_array = generate_random_array_with_ints(-30, 30, 30)
        self.assertTrue(compare_two_array(sorted(random_array), binary_tree.SortTree(binary_tree.BuildBinaryTree(random_array).build_binary_tree()).read_tree_in_order()))

    def test_read_binary_tree_in_order_using_random_array_3(self):
        random_array = generate_random_array_with_ints(-30, 30, 30)
        self.assertTrue(compare_two_array(sorted(random_array), binary_tree.SortTree(binary_tree.BuildBinaryTree(random_array).build_binary_tree()).read_tree_in_order()))

    def test_is_present_in_binary_tree_true(self):
        self.assertTrue(binary_tree.FindNumberInTree(-9, binary_tree.BuildBinaryTree([6, 3, 8, 1, 9, 7, 2, 4, 0, 17, -14, -22, -8, -4, -9,
                                       11]).build_binary_tree()).find_number())

    def test_is_present_in_binary_tree_false(self):
        self.assertFalse(binary_tree.FindNumberInTree(-28, binary_tree.BuildBinaryTree([6, 3, 8, 1, 9, 7, 2, 4, 0, 17, -14, -22, -8, -4, -9,
                                       11]).build_binary_tree()).find_number())


if __name__ == '__main__':
    unittest.main()