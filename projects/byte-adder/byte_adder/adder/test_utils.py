import unittest
import utils


class TestUtils(unittest.TestCase):

    def test_decimal_binary(self):
        result = utils.decimal_binary(10)
        self.assertEqual(result, 1010)

    def test_binary_decimal(self):
        result = utils.binary_decimal(1010)
        self.assertEqual(result, 10)

    def test_xor(self):
        result = utils.XOR(1, 1)
        self.assertEqual(result, 0)

    def test_list_to_string(self):
        result = utils.list_to_String(['a', 'n', 't', 'o', 'n', 6, 9])
        self.assertEqual(result, 'anton69')

    def test_fill_string(self):
        result = utils.fill_string("nton69", num=1, fill='a')
        self.assertEqual(result, "anton69")

    def test_adjust_length(self):
        result = utils.adjust_length("anton69", "anton")
        self.assertEqual(result, ("anton69", "00anton"))


if __name__ == "__main__":
    unittest.main()