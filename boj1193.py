
def find_fraction_num(n):
    line = 1
    total = 0

    # 몇 번째 줄(line)에 속하는지 찾기
    while total + line < n:
        total += line
        line += 1

    offset = n - total - 1

    if line % 2 == 1:
        # 홀수 줄: 위에서 아래로
        x = line - offset
        y = 1 + offset
    else:
        # 짝수 줄: 아래에서 위로
        x = 1 + offset
        y = line - offset

    return x, y


if __name__=="__main__":
    n = int(input())
    x, y = find_fraction_num(n)
    print(f"{x}/{y}")