import unittest
import rail_fence_cipher_encode


class RailFenceCipherDecodeTestCase(unittest.TestCase):
    def test_rail_fence_cipher_decode_happy_path_1(self):
        self.assertEqual(rail_fence_cipher_encode.rail_fence_cipher_encode("WECRLTEERDSOEEFEAOCAIVDEN", 3),
                         "WEAREDISCOVEREDFLEEATONCE")

    def test_rail_fence_cipher_decode_happy_path_2(self):
        self.assertEqual(rail_fence_cipher_encode.rail_fence_cipher_encode("LKIUAJIMKMEKAAUSSDSRTORZBY", 6),
                         "LUKASZRUMAKJESTBOSKIIMADRY")


if __name__ == '__main__':
    unittest.main()
