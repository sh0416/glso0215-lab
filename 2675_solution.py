# 테스트 케이스
T = int(input())

for _ in range(T):
    # 반복 횟수 R, 문자열 S
    R, S = input().split()
    R = int(R)  # R은 정수로 변환

    # 각 문자를 R번 반복하여 새로운 문자열 생성
    P = ''.join(char * R for char in S)

    # 결과 출력
    print(P)