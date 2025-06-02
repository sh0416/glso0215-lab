l1 = list(range(1, 9))
l2 = list(range(8, 0, -1))
l3 = [1, 2, 5, 4, 3, 6, 7, 8]
def music(l):
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
        
music(l1)
music(l2)
music(l3)