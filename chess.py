import sys

def solve():
    input = sys.stdin.readline
    m, n = map(int, input().split())
    board = [input().strip() for _ in range(m)]
    min_repaints = 64

    for i in range(m - 7):
        for j in range(n - 7):
            repaint_count_w = 0
            repaint_count_b = 0

            for row in range(i, i + 8):
                for col in range(j, j + 8):
                    if (row + col) % 2 == 0:
                        if board[row][col] != 'W':
                            repaint_count_w += 1
                        if board[row][col] != 'B':
                            repaint_count_b += 1
                    else:
                        if board[row][col] != 'B':
                            repaint_count_w += 1
                        if board[row][col] != 'W':
                            repaint_count_b += 1
            
            current_min = min(repaint_count_w, repaint_count_b)
            if current_min < min_repaints:
                min_repaints = current_min

    print(min_repaints)

solve()