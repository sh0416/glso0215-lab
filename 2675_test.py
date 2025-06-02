import io
import sys
from contextlib import redirect_stdout

def solve():
    T = int(input())
    for _ in range(T):
        R, S = input().split()
        R = int(R)
        result = ''
        for char in S:
            result += char * R
        print(result)

def test_case_1():
    test_input = "2\n3 ABC\n5 /HTP\n"
    expected_output = "AAABBBCCC\n/////HHHHHTTTTTPPPPP\n"

    # Redirect input and output
    sys.stdin = io.StringIO(test_input)
    output = io.StringIO()
    with redirect_stdout(output):
        solve()

    # Assert result
    assert output.getvalue() == expected_output, f"Expected:\n{expected_output}\nGot:\n{output.getvalue()}"

if __name__ == "__main__":
    test_case_1()
    print("All tests passed.")

