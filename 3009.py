def solution(arr):
    if arr[0] == arr[1]:
        return arr[2]
    else:
        if arr[0] == arr[2]:
            return arr[1]
        else:
            return arr[0]


x = [0 for _ in range(3)]
y = [0 for _ in range(3)]

x[0], y[0] = list(map(int, input().split()))
x[1], y[1] = list(map(int, input().split()))
x[2], y[2] = list(map(int, input().split()))

print(f'{solution(x)} {solution(y)}')