from collections import defaultdict
def graph_coloring(vertices, edges, k, order="input"):
    adj={v:set() for v in vertices}
    for u,v in edges:
        adj[u].add(v); adj[v].add(u)
    order_list=list(vertices)
    if order=="degree":
        order_list=sorted(vertices,key=lambda v:(-len(adj[v]),v))
    colors={}; stats={"nodes":0,"attempts":0,"rejected":0,"backtracks":0,"max_depth":0}
    def search(i):
        stats["nodes"]+=1; stats["max_depth"]=max(stats["max_depth"],i)
        if i==len(order_list): return True
        v=order_list[i]
        for c in range(1,k+1):
            stats["attempts"]+=1
            if all(colors.get(n)!=c for n in adj[v]):
                colors[v]=c
                if search(i+1): return True
                del colors[v]
            else: stats["rejected"]+=1
        stats["backtracks"]+=1
        return False
    ok=search(0)
    return ok, colors if ok else {}, stats
if __name__=="__main__":
    tests=[
      ("Colourable",list(range(5)),[(0,1),(1,2),(2,3),(3,4),(4,0)],3),
      ("Not colourable",list(range(5)),[(i,j) for i in range(5) for j in range(i+1,5)],4),
      ("Boundary: empty graph",list(range(3)),[],1)]
    for name,v,e,k in tests:
      print("\\nTEST:",name," | k =",k)
      for strategy in ("input","degree"):
        ok,col,s=graph_coloring(v,e,k,strategy)
        print(strategy.upper(), "->", "SUCCESS" if ok else "FAIL", "coloring:",col)
        print("stats:",s)
