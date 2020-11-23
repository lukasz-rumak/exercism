import unittest
import quicksort

class LuhnTestCase(unittest.TestCase):
    def test_quicksort_happy_path_1(self):
        self.assertEqual(quicksort.quicksort([3,9,4,6,7,1,2,8,5]), [1,2,3,4,5,6,7,8,9])


if __name__ == '__main__':
    unittest.main()