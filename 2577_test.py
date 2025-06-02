def count_digits_in_product(a, b, c):
    result = str(a * b * c)
    counts = []
    for i in range(10):
        counts.append(result.count(str(i)))
    return counts

# 테스트 1
assert count_digits_in_product(150, 266, 427) == [3,1,0,2,0,0,0,2,0,0]

# 테스트 2
assert count_digits_in_product(1, 1, 1) == [0,1,0,0,0,0,0,0,0,0]

print("모든 테스트 통과")