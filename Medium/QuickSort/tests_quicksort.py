import unittest
import quicksort

class LuhnTestCase(unittest.TestCase):
    def test_quicksort_happy_path_1(self):
        self.assertEqual(quicksort.quicksort([3, 9, 4, 6, 7, 1, 2, 8, 5]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_quicksort_happy_path_2(self):
        self.assertEqual(quicksort.quicksort([6, 15, 4, -6, 7, 5, -2, 8, 1]), [-6, -2, 1, 4, 5, 6, 7, 8, 15])

    def test_quicksort_happy_path_3(self):
        self.assertEqual(quicksort.quicksort([1, 6, 1, 3, 1, 4, 1, 2, 1]), [1, 1, 1, 1, 1, 2, 3, 4, 6])

if __name__ == '__main__':
    unittest.main()