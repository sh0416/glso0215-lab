import sys
input=sys.stdin.readline
a=[]
b=[]
n,m=map(int,input().split())
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    b.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        print(a[i][j]+b[i][j], end=" ")
    print()
