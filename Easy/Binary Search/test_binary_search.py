import unittest
import binary_search


class BinarySearchTestCase(unittest.TestCase):
    def test_binary_search_happy_path_01(self):
        self.assertEqual(binary_search.binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 2), 1)

    def test_binary_search_happy_path_02(self):
        self.assertEqual(binary_search.binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 19), 18)

    def test_binary_search_happy_path_03(self):
        self.assertEqual(binary_search.binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 10), 9)

    def test_binary_search_happy_path_04(self):
        self.assertEqual(binary_search.binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 9), 8)

    def test_binary_search_happy_path_05(self):
        self.assertEqual(binary_search.binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 11), 10)

    def test_binary_search_happy_path_06(self):
        self.assertEqual(binary_search.binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 1), 0)

    def test_binary_search_happy_path_09(self):
        self.assertEqual(binary_search.binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 20), 19)

    def test_binary_search_happy_path_10(self):
        self.assertEqual(binary_search.binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 10), None)

    def test_binary_search_happy_path_11(self):
        self.assertEqual(binary_search.binary_search([1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 2), None)

    def test_binary_search_happy_path_12(self):
        self.assertEqual(binary_search.binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20], 19), None)

    def test_binary_search_happy_path_13(self):
        self.assertEqual(binary_search.binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], 19), 18)

if __name__ == '__main__':
    unittest.main()