import sys
import io

def solve_deque_problem(input_lines_with_n):
    original_stdin = sys.stdin
    simulated_input_str = "\n".join(input_lines_with_n)
    if not simulated_input_str.endswith('\n'):
        simulated_input_str += '\n'
    sys.stdin = io.StringIO(simulated_input_str)

    original_stdout = sys.stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output

    my_list = []
    results = []

    line_n = sys.stdin.readline()
    n = int(line_n.strip())

    for _ in range(n):
        command_line_str = sys.stdin.readline()
        command_line = command_line_str.split()
        
        if not command_line: # 비어 있는 라인 스킵 (최소한의 안전장치)
            continue
            
        command = command_line[0]

        if command == "push_front":
            my_list.insert(0, int(command_line[1]))
        elif command == "push_back":
            my_list.append(int(command_line[1]))
        elif command == "pop_front":
            if my_list:
                results.append(str(my_list.pop(0)))
            else:
                results.append("-1")
        elif command == "pop_back":
            if my_list:
                results.append(str(my_list.pop()))
            else:
                results.append("-1")
        elif command == "size":
            results.append(str(len(my_list)))
        elif command == "empty":
            if not my_list:
                results.append("1")
            else:
                results.append("0")
        elif command == "front":
            if my_list:
                results.append(str(my_list[0]))
            else:
                results.append("-1")
        elif command == "back":
            if my_list:
                results.append(str(my_list[-1]))
            else:
                results.append("-1")

    print("\n".join(results))

    sys.stdin = original_stdin
    sys.stdout = original_stdout

    return captured_output.getvalue().strip()

test_case_name = "BOJ 예제 1 테스트 (리스트 기반 솔루션)"

test_input_lines = [
    "15",
    "push_back 1",
    "push_front 2",
    "front",
    "back",
    "size",
    "empty",
    "pop_front",
    "pop_back",
    "pop_front",
    "size",
    "empty",
    "pop_back",
    "push_front 3",
    "empty",
    "front"
]

expected_output_string = """2
1
2
0
2
1
-1
0
1
-1
0
3"""

if __name__ == "__main__":
    print(f"테스트 케이스 실행: {test_case_name}")
    print("-" * 40)

    actual_output_string = solve_deque_problem(test_input_lines)

    print("예상 출력:")
    print("---")
    print(expected_output_string)
    print("---")

    print("\n실제 출력:")
    print("---")
    print(actual_output_string)
    print("---")

    if actual_output_string.strip() == expected_output_string.strip():
        print("\n결과: 동일")
    else:
        print("\n결과: 실패")

    print("-" * 40)
