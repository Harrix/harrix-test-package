import unittest

import harrixtestpackage as h

class TestHarrixTestPackage(unittest.TestCase):

    def test_multiply_2(self):
        re = h.multiply_2(2)
        self.assertEqual(re, 4)

    def test_multiply_10(self):
        re = h.multiply_10(2)
        self.assertEqual(re, 20)

    def test_multiply_20(self):
        re = h.multiply_20(2)
        self.assertEqual(re, 40)

    def test_multiply_30(self):
        re = h.multiply_30(2)
        self.assertEqual(re, 60)


if __name__ == '__main__':
    unittest.main()
