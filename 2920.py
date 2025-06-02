l = list(map(int, input().split()))
count_as = 0
count_ds = 0
for i in range(1, 9):
    if l[i - 1] == i:
        count_as += 1
    if l[i - 1] == 9 - i:
        count_ds += 1

if count_as == 8:
    print('ascending')
elif count_ds == 8:
    print('descending')
else:
    print('mixed')