import sys
tc=int(sys.stdin.readline().rstrip())

for i in range(tc):
    sel=0
    n,m=map(int,sys.stdin.readline().rstrip().split())
    pk=list(map(int,sys.stdin.readline().rstrip().split()))
    pl={k:p for k,p in enumerate(pk)}
    c=0
    mp=max(pl.values())
    while pl[m]!=0:
        if pl[sel]==mp:
            pl[sel]=0
            mp=max(pl.values())
            c+=1
            if sel==len(pl)-1:
                sel=0
        else:
            if sel==len(pl)-1:
                sel=0
            else:
                sel+=1
    print(c)
