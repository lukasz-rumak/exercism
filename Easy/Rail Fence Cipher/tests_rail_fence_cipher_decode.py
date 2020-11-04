import unittest
import rail_fence_cipher_decode


class RailFenceCipherDecodeTestCase(unittest.TestCase):
    def test_rail_fence_cipher_decode_happy_path_1(self):
        self.assertEqual(rail_fence_cipher_decode.rail_fence_cipher_decode("WECRLTEERDSOEEFEAOCAIVDEN", 3),
                         "WEAREDISCOVEREDFLEEATONCE")

    def test_rail_fence_cipher_decode_happy_path_2(self):
        self.assertEqual(rail_fence_cipher_decode.rail_fence_cipher_decode("LKIUAJIMKMEKAAUSSDSRTORZBY", 6),
                         "LUKASZRUMAKJESTBOSKIIMADRY")


if __name__ == '__main__':
    unittest.main()
