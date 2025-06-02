import unittest
import importlib

# this is necessary to import from an invalid file name
module_2941 = importlib.import_module("2941")
count_croatian_letters = module_2941.count_croatian_letters

# tests
class TestCroatianAlphabet(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_croatian_letters(""), 0)

    def test_single_letters(self):
        self.assertEqual(count_croatian_letters("abc"), 3)

    def test_simple_croatian_letters(self):
        self.assertEqual(count_croatian_letters("c="), 1)
        self.assertEqual(count_croatian_letters("c-"), 1)
        self.assertEqual(count_croatian_letters("dz="), 1)
        self.assertEqual(count_croatian_letters("lj"), 1)
        self.assertEqual(count_croatian_letters("nj"), 1)
        self.assertEqual(count_croatian_letters("s="), 1)
        self.assertEqual(count_croatian_letters("z="), 1)

    # 백준 test cases

    def test_baekjoon_1(self):
        self.assertEqual(count_croatian_letters("ljes=njak"), 6) 

    def test_baekjoon_2(self):
        self.assertEqual(count_croatian_letters("ddz=z="), 3) # d, dz=, z=

    def test_baekjoon_3(self):
        self.assertEqual(count_croatian_letters("nljj"), 3) # n, lj, j

    def test_partial_match_at_end(self):
        self.assertEqual(count_croatian_letters("abclj"), 4) # a, b, c, lj
        self.assertEqual(count_croatian_letters("abcdz"), 5) # a, b, c, d, z
        
    def test_baekjoon_4(self):
        self.assertEqual(count_croatian_letters("c=c="), 2)

    def test_baekjoon_5(self):
        self.assertEqual(count_croatian_letters("dz=ak"), 3)

if __name__ == '__main__':
    unittest.main()