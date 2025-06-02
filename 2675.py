# Read number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    R, S = input().split()
    R = int(R)
    result = ''
    for char in S:
        result += char * R
    print(result)
