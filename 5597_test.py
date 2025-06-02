import unittest
from io import StringIO
import sys

def find_missing_students(input_data):
    submitted = set(map(int, input_data.strip().split()))
    missing = [i for i in range(1, 31) if i not in submitted]
    missing.sort()
    return missing

class TestMissingStudents(unittest.TestCase):
    def test_case1(self):
        # 제출하지 않은 번호: 2, 8
        input_data = ' '.join(str(i) for i in range(1, 31) if i not in (2, 8))
        expected = [2, 8]
        self.assertEqual(find_missing_students(input_data), expected)

    def test_case2(self):
        # 제출하지 않은 번호: 29, 30
        input_data = ' '.join(str(i) for i in range(1, 29))
        expected = [29, 30]
        self.assertEqual(find_missing_students(input_data), expected)

    def test_case3(self):
        # 제출하지 않은 번호: 1, 30
        input_data = ' '.join(str(i) for i in range(2, 30))
        expected = [1, 30]
        self.assertEqual(find_missing_students(input_data), expected)

if __name__ == '__main__':
    unittest.main()
