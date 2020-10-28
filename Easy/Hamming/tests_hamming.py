import unittest
import hamming

class HammingTestCase(unittest.TestCase):
    def test_hamming_happy_path_1(self):
        self.assertEqual(hamming.calculate_hamming_distance("GAGCCTACTAACGGGAT","CATCGTAATGACGGCCT"), 7)

    def test_hamming_happy_path_2(self):
        self.assertEqual(hamming.calculate_hamming_distance("GAGCCTACTAACGGGATAAAG","CATCGTAATGACGGCCTCCTT"), 11)

    def test_hamming_happy_path_3(self):
        self.assertEqual(hamming.calculate_hamming_distance("GAGCCTACTAACGGGAT","GAGCCTACTAACGGGAT"), 0)

    def test_hamming_no_data_for_both(self):
        self.assertEqual(hamming.calculate_hamming_distance("",""), "Please provide valid data. Reason: no data.")

    def test_hamming_no_data_for_second(self):
        self.assertEqual(hamming.calculate_hamming_distance("GAGCCTACTAACGGGAT", ""), "Please provide valid data. Reason: no data.")

    def test_hamming_diff_length(self):
        self.assertEqual(hamming.calculate_hamming_distance("GAGCCTACTAACGGGAT","CATCGTAATGACGG"), "Please provide valid data. Reason: diff length.")

    def test_hamming_incorrect_character_1(self):
        self.assertEqual(hamming.calculate_hamming_distance("GAGCCTACTXACGGGAT", "CATCCTAATGACGGCCT"), "Please provide valid data. Reason: incorrect character(s).")

    def test_hamming_incorrect_character_1(self):
        self.assertEqual(hamming.calculate_hamming_distance("GAGCCTACTAACGGGAT", "CATCCTAATXACGGCCT"), "Please provide valid data. Reason: incorrect character(s).")

if __name__ == '__main__':
    unittest.main()