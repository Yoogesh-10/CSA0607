# Task 6: TSP Held-Karp DP
from itertools import permutations
from time import perf_counter
def held_karp(cost):
    n=len(cost); hub=0; others=list(range(1,n)); full=(1<<len(others))-1
    dp={}; parent={}; states=0
    for j in others:
        mask=1<<(j-1);dp[(mask,j)]=cost[hub][j];parent[(mask,j)]=hub;states+=1
    for mask in range(1,full+1):
        for j in others:
            if not mask&(1<<(j-1)) or (mask,j) not in dp:continue
            for k in others:
                if mask&(1<<(k-1)):continue
                nm=mask|(1<<(k-1)); cand=dp[(mask,j)]+cost[j][k]
                if (nm,k) not in dp or cand<dp[(nm,k)]:
                    dp[(nm,k)]=cand;parent[(nm,k)]=j;states+=1
    best=min(dp[(full,j)]+cost[j][hub] for j in others)
    end=min(others,key=lambda j:dp[(full,j)]+cost[j][hub])
    route=[end];mask=full;j=end
    while mask:
        prev=parent[(mask,j)]
        mask^=1<<(j-1)
        if prev==hub:break
        route.append(prev);j=prev
    route.reverse()
    return [hub]+route+[hub],best,states,dp,parent
def brute(cost):
    n=len(cost)
    best=float("inf");route=None
    for p in permutations(range(1,n)):
        r=(0,)+p+(0,);v=sum(cost[r[i]][r[i+1]] for i in range(len(r)-1))
        if v<best:best=v;route=r
    return route,best
def make_cost(n,seed=10):
    import random
    random.seed(seed)
    m=[[0 if i==j else random.randint(2,30) for j in range(n)] for i in range(n)]
    return m
def run(n):
    c=make_cost(n)
    st=perf_counter();r,v,s,dp,par=held_karp(c);elapsed=perf_counter()-st
    print(f"n={n} locations incl hub; states={s}; time={elapsed:.6f}s; route={r}; cost={v}; approx DP entries={len(dp)}")
    return c,r,v,s,elapsed
if __name__=="__main__":
    cost=make_cost(7)
    print("COST MATRIX")
    for row in cost:print(row)
    route,val,states,dp,parent=held_karp(cost)
    print("OPTIMAL ROUTE:",route,"cost:",val,"states:",states)
    small=make_cost(5);broute,bval=brute(small);droute,dval,*_=held_karp(small)
    print("VALIDATION 5 vertices: brute force",broute,bval,"DP",droute,dval,"MATCH",bval==dval)
    print("STATE SPACE EXPERIMENT")
    for n in range(4,10):run(n)
    print("Boundary: one location (hub only)")
    print("Hub->Hub cost=0")
