import unittest
import rail_fence_cipher


class RailFenceCipherTestCase(unittest.TestCase):
    def test_rail_fence_cipher_happy_path_1(self):
        self.assertEqual(rail_fence_cipher.rail_fence_cipher("WE ARE DISCOVERED. FLEE AT ONCE", 3),
                         "WECRLTEERDSOEEFEAOCAIVDEN")

    def test_rail_fence_cipher_happy_path_2(self):
        self.assertEqual(rail_fence_cipher.rail_fence_cipher("LUKASZ RUMAK JEST BOSKI I MADRY.", 6),
                         "LKIUAJIMKMEKAAUSSDSRTORZBY")


if __name__ == '__main__':
    unittest.main()
