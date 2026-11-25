# Task 5: Kruskal, Prim and Boruvka MST
class DSU:
    def __init__(self,n):self.p=list(range(n));self.r=[0]*n
    def find(self,x):
        if self.p[x]!=x:self.p[x]=self.find(self.p[x])
        return self.p[x]
    def union(self,a,b):
        a=self.find(a);b=self.find(b)
        if a==b:return False
        if self.r[a]<self.r[b]:a,b=b,a
        self.p[b]=a
        if self.r[a]==self.r[b]:self.r[a]+=1
        return True
def kruskal(V,E):
    d=DSU(len(V));out=[];trace=[]
    for u,v,w in sorted(E,key=lambda x:x[2]):
        if d.union(V.index(u),V.index(v)):out.append((u,v,w));trace.append(("accept",u,v,w))
        else:trace.append(("reject-cycle",u,v,w))
    return out,trace
def prim(V,E,start):
    adj={v:[] for v in V}
    for u,v,w in E:adj[u].append((w,u,v));adj[v].append((w,v,u))
    seen={start};out=[];trace=[];heap=adj[start][:]
    import heapq;heapq.heapify(heap)
    while heap and len(seen)<len(V):
        w,u,v=heapq.heappop(heap)
        if v in seen:continue
        seen.add(v);out.append((u,v,w));trace.append((u,v,w))
        for e in adj[v]:
            if e[2] not in seen:heapq.heappush(heap,e)
    return out,trace
def boruvka(V,E):
    d=DSU(len(V));out=[];trace=[]
    while len(out)<len(V)-1:
        cheapest={}
        for u,v,w in E:
            a=d.find(V.index(u));b=d.find(V.index(v))
            if a!=b:
                if a not in cheapest or w<cheapest[a][2]:cheapest[a]=(u,v,w)
                if b not in cheapest or w<cheapest[b][2]:cheapest[b]=(u,v,w)
        added=0
        for edge in cheapest.values():
            u,v,w=edge
            if d.union(V.index(u),V.index(v)):out.append(edge);trace.append(edge);added+=1
        if added==0:break
    return out,trace
def show(name,out,trace):
    print(name,"construction trace:",trace)
    print("MST edges:",out,"cost:",sum(x[2] for x in out))
if __name__=="__main__":
    V=list("ABCDEFGH")
    E=[("A","B",4),("A","C",3),("B","C",1),("B","D",5),("C","D",4),("C","E",6),("D","E",2),("D","F",7),("E","F",3),("E","G",8),("F","G",4),("G","H",2),("F","H",6),("B","H",9)]
    print("BASE GRAPH")
    for fn in [kruskal]:
        out,tr=fn(V,E);show("Kruskal",out,tr)
    out,tr=prim(V,E,"A");show("Prim",out,tr)
    out,tr=boruvka(V,E);show("Boruvka",out,tr)
    print("\nMULTIPLE MST TEST: change A-C and B-C to equal weight 1")
    E2=[(u,v,(1 if (u,v) in [("A","C"),("B","C")] else w)) for u,v,w in E]
    for name,fn in [("Kruskal",kruskal),("Boruvka",boruvka)]:
        o,t=fn(V,E2);show(name,o,t)
    print("Prim:",prim(V,E2,"A")[0])
