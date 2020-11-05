import unittest
import rail_fence_cipher_decode


class RailFenceCipherDecodeTestCase(unittest.TestCase):
    def test_rail_fence_cipher_decode_happy_path_1(self):
        self.assertEqual(rail_fence_cipher_decode.rail_fence_cipher_decode("WECRLTEERDSOEEFEAOCAIVDEN", 3),
                         "WEAREDISCOVEREDFLEEATONCE")

    def test_rail_fence_cipher_decode_happy_path_2(self):
        self.assertEqual(rail_fence_cipher_decode.rail_fence_cipher_decode("LKIUAJIMKMEKAAUSSDSRTORZBY", 6),
                         "LUKASZRUMAKJESTBOSKIIMADRY")

    def test_rail_fence_cipher_decode_happy_path_3(self):
        self.assertEqual(rail_fence_cipher_decode.rail_fence_cipher_decode("LKIUAJIMJKMEKAAAUSSDFSRTORIZBY", 6),
                         "LUKASZRUMAKJESTBOSKIIMADRYIFAJ")

    def test_rail_fence_cipher_decode_happy_path_4(self):
        self.assertEqual(rail_fence_cipher_decode.rail_fence_cipher_decode("LKINUAJIMJKMEKAAAUSSDFSRTORIZBY", 6),
                         "LUKASZRUMAKJESTBOSKIIMADRYIFAJN")

    def test_rail_fence_cipher_decode_happy_path_5(self):
        self.assertEqual(rail_fence_cipher_decode.rail_fence_cipher_decode("LKINUAJIMJYKMEKAAAUSSDFSRTORIZBY", 6),
                         "LUKASZRUMAKJESTBOSKIIMADRYIFAJNY")

    def test_rail_fence_cipher_decode_happy_path_6(self):
        self.assertEqual(rail_fence_cipher_decode.rail_fence_cipher_decode("LKSRMKUAZUA", 2),
                         "LUKASZRUMAK")

    def test_rail_fence_cipher_decode_happy_path_7(self):
        self.assertEqual(rail_fence_cipher_decode.rail_fence_cipher_decode("LSMUAZUAKRK", 3),
                         "LUKASZRUMAK")

    def test_rail_fence_cipher_decode_happy_path_8(self):
        self.assertEqual(rail_fence_cipher_decode.rail_fence_cipher_decode("LRUZUKSMKAA", 4),
                         "LUKASZRUMAK")

    def test_rail_fence_cipher_decode_happy_path_9(self):
        self.assertEqual(rail_fence_cipher_decode.rail_fence_cipher_decode("LMUUAKRKAZS", 5),
                         "LUKASZRUMAK")

    def test_rail_fence_cipher_decode_happy_path_10(self):
        self.assertEqual(rail_fence_cipher_decode.rail_fence_cipher_decode("LKUAKMAUSRZ", 6),
                         "LUKASZRUMAK")

    def test_rail_fence_cipher_decode_happy_path_11(self):
        self.assertEqual(rail_fence_cipher_decode.rail_fence_cipher_decode("LUKKAASMZUR", 7),
                         "LUKASZRUMAK")

    def test_rail_fence_cipher_decode_happy_path_12(self):
        self.assertEqual(rail_fence_cipher_decode.rail_fence_cipher_decode("LUKASKZARMU", 8),
                         "LUKASZRUMAK")


if __name__ == '__main__':
    unittest.main()
