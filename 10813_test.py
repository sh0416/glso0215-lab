def solution():
    with open("10813_test_input.txt", "r") as f:
        n, m = map(int, f.readline().split())
        baskets = list(range(1, n + 1))

        for _ in range(m):
            i, j = map(int, f.readline().split())
            baskets[i - 1], baskets[j - 1] = baskets[j - 1], baskets[i - 1]

        print(*baskets)

# 테스트 실행
if __name__ == "__main__":
    solution()

