submitted = set()

# 입력: 28명의 제출자 번호를 입력받아 set에 저장
for _ in range(28):
    n = int(input())
    submitted.add(n)

# 전체 출석번호(1~30) 중 제출하지 않은 번호 찾기
missing = [i for i in range(1, 31) if i not in submitted]

# 오름차순으로 출력
missing.sort()
print(missing[0])
print(missing[1])
