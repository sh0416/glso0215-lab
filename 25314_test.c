#include <stdio.h>

void test_case(int N, const char* expected_output) {
    printf("입력: %d\n", N);
    printf("기대한 출력: %s\n", expected_output);

    // 프로그램 로직 수행
    int i;
    for (i = N / 4; i > 0; i--)
        printf("long ");
    printf("int\n");

    printf("------------\n");
}

int main() {
    // 예제 테스트 케이스
    test_case(4, "long int");
    test_case(20, "long long long long long int");
    test_case(0, "int");
    test_case(8, "long long int");
    test_case(16, "long long long long int");

    return 0;
}
