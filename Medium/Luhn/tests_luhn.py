import unittest
import luhn

class LuhnTestCase(unittest.TestCase):
    def test_luhn_true_1(self):
        self.assertEqual(luhn.calculate_luhn("4539148803436467"), True)

    def test_luhn_true_2(self):
        self.assertEqual(luhn.calculate_luhn("3530710615676894"), True)

    def test_luhn_true_3(self):
        self.assertEqual(luhn.calculate_luhn("6394888020170352"), True)

    def test_luhn_false_1(self):
        self.assertEqual(luhn.calculate_luhn("8273123273520569"), False)

    def test_luhn_false_2(self):
        self.assertEqual(luhn.calculate_luhn("3530710635676894"), False)

    def test_luhn_false_3(self):
        self.assertEqual(luhn.calculate_luhn("6396888020170352"), False)

    def test_luhn_validation_error_1(self):
        self.assertEqual(luhn.calculate_luhn("82731232735205691"), "Please provide valid card number.")

    def test_luhn_validation_error_2(self):
        self.assertEqual(luhn.calculate_luhn("827312327"), "Please provide valid card number.")

    def test_luhn_validation_error_3(self):
        self.assertEqual(luhn.calculate_luhn("45391488x3436467"), "Please provide valid card number.")

    def test_luhn_validation_error_4(self):
        self.assertEqual(luhn.calculate_luhn("4a3b1c8dxe4f6g6h"), "Please provide valid card number.")

    def test_luhn_validation_error_5(self):
        self.assertEqual(luhn.calculate_luhn("!@#$%^&*()!@#$%^"), "Please provide valid card number.")


if __name__ == '__main__':
    unittest.main()