import sys

def f(n,a):
    INF=999999
    d=[[INF]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j]==-1:
                d[i][j]=INF
            else:
                d[i][j]=a[i][j]
        d[i][i]=0
    for k in range(n):
        for i in range(n):
            if d[i][k]==INF:
                continue
            for j in range(n):
                if d[k][j]==INF:
                    continue
                if d[i][j]>d[i][k]+d[k][j]:
                    d[i][j]=d[i][k]+d[k][j]
    return d

def p(m):
    for r in m:
        o=[]
        for x in r:
            if x>=999999:
                o.append("-1")
            else:
                o.append(str(x))
        print(' '.join(o))

def main():
    n=int(sys.stdin.readline().strip())
    a=[]
    for _ in range(n):
        a.append(list(map(int,sys.stdin.readline().split())))
    p(f(n,a))

if __name__=="__main__":
    main()
