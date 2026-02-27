import heapq
import sys

def f(n,m,s,t,e):
    g=[[]for _ in range(n)]
    for u,v,d in e:
        g[u].append((v,d))
    INF=float('inf')
    dist=[INF]*n
    p=[-1]*n
    dist[s]=0
    q=[(0,s)]
    while q:
        d_u,u=heapq.heappop(q)
        if u==t and d_u<=dist[t]:
            break
        if d_u>dist[u]:
            continue
        for v,w in g[u]:
            nd=dist[u]+w
            if nd<dist[v]:
                dist[v]=nd
                p[v]=u
                heapq.heappush(q,(nd,v))
    if dist[t]==INF:
        return "Ne mogu naiti marshrut! :'("
    path=[]
    cur=t
    while cur!=-1:
        path.append(cur)
        cur=p[cur]
    path.reverse()
    return f"{int(dist[t])}\n{' '.join(map(str,path))}"

def main():
    l=sys.stdin.readline().strip()
    if not l:
        return
    n,m,s,t=map(int,l.split())
    e=[]
    for _ in range(m):
        u,v,d=map(int,sys.stdin.readline().split())
        e.append((u,v,d))
    print(f(n,m,s,t,e))

if __name__=="__main__":
    main()
