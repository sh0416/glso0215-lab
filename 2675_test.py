# 테스트 케이스 파일입니다.
# input.txt 파일을 
# 파일에서 입력 읽기

# 예상 출력 결과를 저장하는 배열

expected_output_result = []
with open('text_case_expected_output.txt') as f:
    expected_output_result = [line.strip() for line in f.readlines()]

# 출력 결과를 저장하는 배열
output_result = []

with open('test_case_input.txt', 'r') as f:
    T = int(f.readline())
    for _ in range(T):
        R, S = f.readline().split()
        R = int(R)
        P = ''.join(char * R for char in S)
        output_result.append(P)

all_match = True
for i, (expected, actual) in enumerate(zip(expected_output_result, output_result), 1):
    if expected != actual:
        print(f"Test case {i} failed:")
        print(f"Expected: {expected}")
        print(f"Actual:   {actual}")
        all_match = False
    else:
        print(f"Test case {i} passed")

if all_match:
    print("All test cases passed!")
else:
    print("Some test cases failed.")