import unittest

def matrix_addition(n, m, matrix_a, matrix_b):
    result = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)
    return result

class TestMatrixAddition(unittest.TestCase):
    def test_case_1(self):
        n, m = 3, 3
        matrix_a = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        matrix_b = [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]
        expected = [
            [10, 10, 10],
            [10, 10, 10],
            [10, 10, 10]
        ]
        self.assertEqual(matrix_addition(n, m, matrix_a, matrix_b), expected)

    def test_case_2(self):
        n, m = 1, 1
        matrix_a = [[5]]
        matrix_b = [[10]]
        expected = [[15]]
        self.assertEqual(matrix_addition(n, m, matrix_a, matrix_b), expected)

    def test_case_3(self):
        n, m = 2, 4
        matrix_a = [
            [1, 3, 5, 7],
            [9, 11, 13, 15]
        ]
        matrix_b = [
            [2, 4, 6, 8],
            [10, 12, 14, 16]
        ]
        expected = [
            [3, 7, 11, 15],
            [19, 23, 27, 31]
        ]
        self.assertEqual(matrix_addition(n, m, matrix_a, matrix_b), expected)

if __name__ == "__main__":
    unittest.main()

