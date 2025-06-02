def solution(arr):
    if arr[0] == arr[1]:
        return arr[2]
    else:
        if arr[0] == arr[2]:
            return arr[1]
        else:
            return arr[0]

# test case 1
x = [1, 2, 1]
y = [1, 2, 2]
assert solution(x) == 2
assert solution(y) == 1

# test case 2
x = [4, 4, 8]
y = [10, 5, 10]
assert solution(x) == 8
assert solution(y) == 5

# test case 3
x = [100, 100, 200]
y = [100, 200, 100]
assert solution(x) == 200
assert solution(y) == 200

print("All tests passed")
