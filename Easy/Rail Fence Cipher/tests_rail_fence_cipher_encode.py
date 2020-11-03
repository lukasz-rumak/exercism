import unittest
import rail_fence_cipher_encode


class RailFenceCipherEncodeTestCase(unittest.TestCase):
    def test_rail_fence_cipher_encode_happy_path_1(self):
        self.assertEqual(rail_fence_cipher_encode.rail_fence_cipher_encode("WE ARE DISCOVERED. FLEE AT ONCE", 3),
                         "WECRLTEERDSOEEFEAOCAIVDEN")

    def test_rail_fence_cipher_encode_happy_path_2(self):
        self.assertEqual(rail_fence_cipher_encode.rail_fence_cipher_encode("LUKASZ RUMAK JEST BOSKI I MADRY.", 6),
                         "LKIUAJIMKMEKAAUSSDSRTORZBY")


if __name__ == '__main__':
    unittest.main()
