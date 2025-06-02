def calculate_score(quiz):
    score = 0
    consecutive_o = 0
    
    for char in quiz:
        if char == 'O':
            consecutive_o += 1
            score += consecutive_o
        else:
            consecutive_o = 0
            
    return score

# 입력 받기
test_case_count = int(input())  # 첫 줄에 테스트 케이스 개수 입력

for _ in range(test_case_count):
    quiz_result = input().strip()  # OX 문자열 입력
    print(calculate_score(quiz_result))
