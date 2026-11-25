# Task 3: Dijkstra, Bellman-Ford, Floyd and Warshall
import heapq, math
INF=math.inf
def dijkstra(g,src):
    dist={v:INF for v in g}; pred={v:None for v in g}; dist[src]=0
    pq=[(0,src)]; final=[]
    while pq:
        d,u=heapq.heappop(pq)
        if d!=dist[u]: continue
        final.append(u)
        for v,w in g[u]:
            if dist[u]+w<dist[v]:
                dist[v]=dist[u]+w; pred[v]=u; heapq.heappush(pq,(dist[v],v))
    return dist,pred,final
def path(pred,v):
    out=[]
    while v is not None: out.append(v); v=pred[v]
    return " -> ".join(reversed(out))
def bellman(g,src):
    edges=[(u,v,w) for u in g for v,w in g[u]]
    d={v:INF for v in g}; p={v:None for v in g}; d[src]=0
    for _ in range(len(g)-1):
        changed=False
        for u,v,w in edges:
            if d[u]!=INF and d[u]+w<d[v]: d[v]=d[u]+w;p[v]=u;changed=True
        if not changed: break
    neg=any(d[u]!=INF and d[u]+w<d[v] for u,v,w in edges)
    return d,p,neg
def floyd(vertices,edges):
    n=len(vertices); idx={v:i for i,v in enumerate(vertices)}
    d=[[INF]*n for _ in range(n)]
    for i in range(n): d[i][i]=0
    for u,v,w in edges: d[idx[u]][idx[v]]=min(d[idx[u]][idx[v]],w)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k]+d[k][j]<d[i][j]:d[i][j]=d[i][k]+d[k][j]
    return d
def warshall(vertices,edges):
    n=len(vertices);idx={v:i for i,v in enumerate(vertices)}
    r=[[False]*n for _ in range(n)]
    for i in range(n):r[i][i]=True
    for u,v,w in edges:r[idx[u]][idx[v]]=True
    for k in range(n):
        for i in range(n):
            for j in range(n):r[i][j]=r[i][j] or (r[i][k] and r[k][j])
    return r
def showmatrix(vertices,m):
    print("   "+" ".join(vertices))
    for v,row in zip(vertices,m):
        print(v, " ".join("∞" if x==INF else str(x) for x in row))
if __name__=="__main__":
    V=list("ABCDEFGH")
    E=[("A","B",4),("A","C",7),("B","C",2),("B","D",6),("C","D",1),("C","E",8),("D","E",3),("D","F",5),("E","F",2),("E","G",6),("F","G",1),("G","H",2),("F","H",7)]
    G={v:[] for v in V}
    for u,v,w in E:G[u].append((v,w));G[v].append((u,w))
    print("NORMAL Dijkstra from A")
    d,p,order=dijkstra(G,"A")
    for v in V:print(v,d[v],path(p,v), "pred=",p[v])
    print("Finalisation order:",order)
    print("\nMEANINGFUL NEGATIVE-EDGE DEMO: A->B=10, A->C=5, B->C=-8, C->B=10")
    demo={"A":[("B",10),("C",5)],"B":[("C",-8)],"C":[("B",10)]}
    # Standard Dijkstra with a finalized set illustrates why negative weights invalidate the greedy finalisation.
    dd={v:INF for v in demo};dd["A"]=0;pp={v:None for v in demo};done=set();order=[]
    while len(done)<len(demo):
        u=min((v for v in demo if v not in done),key=lambda v:dd[v])
        if dd[u]==INF:break
        done.add(u);order.append(u)
        for v,w in demo[u]:
            if v not in done and dd[u]+w<dd[v]:dd[v]=dd[u]+w;pp[v]=u
    fd,fp,fn=bellman(demo,"A")
    print("Dijkstra finalised order:",order,"distances:",dd)
    print("Bellman-Ford distances:",fd,"negative cycle:",fn)
    print("Affected decision: C is finalised at 5 before B; B->C=-8 later offers C=2, but finalized Dijkstra refuses to revise C.")
    print("\nNEGATIVE EDGE (H->A = -3) Bellman-Ford directed variant")
    directed={v:[] for v in V}
    for u,v,w in E:directed[u].append((v,w))
    directed["H"].append(("A",-3))
    bd,bp,neg=bellman(directed,"A")
    print("Bellman-Ford distances:",bd,"negative cycle:",neg)
    print("Dijkstra validity: invalid for negative edge; settled A can be improved through A-B-C-D-F-G-H-A.")
    print("\nNEGATIVE CYCLE TEST: add A->B=-2 and B->A=-2")
    cyc={v:list(directed[v]) for v in V};cyc["A"].append(("B",-2));cyc["B"].append(("A",-2))
    cd,cp,cneg=bellman(cyc,"A");print("Negative cycle detected:",cneg)
    print("\nFloyd-Warshall distance matrix (undirected normal graph)")
    showmatrix(V,floyd(V,E))
    print("\nWarshall reachability matrix")
    showmatrix(V,warshall(V,E))
