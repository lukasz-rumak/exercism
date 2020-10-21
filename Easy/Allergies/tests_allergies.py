import unittest
import allergies

class AllergiesTestCase(unittest.TestCase):
    def test_allergies_for_string(self):
        self.assertEqual(allergies.return_allergies("asd"), "Please provide valid input.")

    def test_allergies_for_minus_128(self):
        self.assertEqual(allergies.return_allergies(-128), "Please provide valid input.")

    def test_allergies_for_0(self):
        self.assertEqual(allergies.return_allergies(0), "Please provide valid input.")

    def test_allergies_for_1(self):
        self.assertEqual(allergies.return_allergies(1), ["eggs"])

    def test_allergies_for_9(self):
        self.assertEqual(allergies.return_allergies(9), ["strawberries", "eggs"])

    def test_allergies_for_64(self):
        self.assertEqual(allergies.return_allergies(64), ["pollen"])

    def test_allergies_for_130(self):
        self.assertEqual(allergies.return_allergies(130), ["cats", "peanuts"])

    def test_allergies_for_255(self):
        self.assertEqual(allergies.return_allergies(255), ["cats", "pollen", "chocolate", "tomatoes", "strawberries", "shellfish", "peanuts", "eggs"])

    def test_allergies_for_256(self):
        self.assertEqual(allergies.return_allergies(256), ["Unknown"])

    def test_allergies_for_260(self):
        self.assertEqual(allergies.return_allergies(260), ["Unknown", "shellfish"])

    def test_allergies_for_512(self):
        self.assertEqual(allergies.return_allergies(512), ["Unknown"])

    def test_allergies_for_3055(self):
        self.assertEqual(allergies.return_allergies(2055), ["Unknown", "shellfish", "peanuts", "eggs"])

    def test_allergies_for_9852(self):
        self.assertEqual(allergies.return_allergies(985752), ["Unknown", "Unknown", "Unknown", "Unknown", "Unknown", "Unknown", "cats", "tomatoes", "strawberries"])


if __name__ == '__main__':
    unittest.main()
