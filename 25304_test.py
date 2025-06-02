import unittest
from unittest.mock import patch
import io
import sys
import importlib.util

# 파일 경로를 사용하여 모듈을 동적으로 로드합니다.
def load_module_from_file(file_path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None:
        raise FileNotFoundError(f"Could not find module file: {file_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module # 모듈을 sys.modules에 추가
    spec.loader.exec_module(module)
    return module

# 25304.py 로드
try:
    # 이 테스트 파일과 25304.py가 같은 디렉토리에 있다고 가정합니다.
    problem_module = load_module_from_file("25304.py", "problem_25304")
    calculate_total_spent = problem_module.calculate_total_spent
    main_function = problem_module.main # main 함수를 가져옵니다.
except FileNotFoundError:
    print("오류: 25304.py 파일을 찾을 수 없습니다. 테스트 파일과 같은 디렉토리에 있는지 확인해주세요.")
    def calculate_total_spent(*args, **kwargs): raise RuntimeError("25304.py 로드 실패 - 파일 없음")
    def main_function(*args, **kwargs): raise RuntimeError("25304.py 로드 실패 - 파일 없음")
except Exception as e:
    print(f"25304.py 모듈 로드 중 예외 발생: {e}") # 여기서 e는 사용 가능
    # 아래 RuntimeError에서는 직접 e를 참조하지 않도록 수정
    def calculate_total_spent(*args, **kwargs): raise RuntimeError("25304.py 로드 중 일반 오류 발생")
    def main_function(*args, **kwargs): raise RuntimeError("25304.py 로드 중 일반 오류 발생")

class TestReceiptVerification(unittest.TestCase):

    @patch('builtins.input')
    def test_calculate_total_spent_no_items(self, mock_input):
        self.assertEqual(calculate_total_spent(0), 0)

    @patch('builtins.input')
    def test_calculate_total_spent_one_item(self, mock_input):
        mock_input.side_effect = ["1000 2"]
        self.assertEqual(calculate_total_spent(1), 2000)

    @patch('builtins.input')
    def test_calculate_total_spent_multiple_items(self, mock_input):
        mock_input.side_effect = ["20000 5", "3000 2", "1000 1"]
        self.assertEqual(calculate_total_spent(3), 100000 + 6000 + 1000)

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_yes_case(self, mock_stdout, mock_input):
        # 25304.py의 main 함수를 직접 테스트
        mock_input.side_effect = ["260000", "4", "20000 5", "30000 2", "10000 6", "5000 8"]
        main_function() # main_logic 대신 main_function 호출
        self.assertEqual(mock_stdout.getvalue().strip(), "Yes")

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_no_case(self, mock_stdout, mock_input):
        # 25304.py의 main 함수를 직접 테스트
        mock_input.side_effect = ["250000", "4", "20000 5", "30000 2", "10000 6", "5000 8"]
        main_function() # main_logic 대신 main_function 호출
        self.assertEqual(mock_stdout.getvalue().strip(), "No")

if __name__ == '__main__':
    # 25304.py 파일이 정상적으로 로드되었는지 확인 후 테스트 실행
    if 'problem_module' in globals() and hasattr(problem_module, 'main'):
        print("25304.py 모듈이 로드되었습니다. 테스트를 실행합니다.")
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
    else:
        print("25304.py 모듈 또는 main 함수 로드에 실패하여 테스트를 실행할 수 없습니다.")