n, m = map(int, input().split())

baskets = [i for i in range (1, n+1)]

for _ in range (m):
    i, j = map(int, input().split())
    baskets[i - 1], baskets[j - 1] = baskets[j - 1], baskets[i - 1]

print(*baskets)

파일 이름을 `문제번호.py` 또는 `문제번호.ccp`와 같은 형식으로 작성해주세요. 