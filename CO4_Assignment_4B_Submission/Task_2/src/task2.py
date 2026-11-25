# Task 2: Fractional Greedy vs 0/1 Knapsack DP
def fractional(items, capacity):
    items=sorted(items,key=lambda x:x[2]/x[1],reverse=True)
    remaining=capacity; value=0; chosen=[]; operations=0
    for name,w,v in items:
        operations+=1
        if remaining<=0: break
        frac=min(1,remaining/w)
        if frac>0:
            chosen.append((name,frac,w*frac,v*frac,v/w))
            value+=v*frac; remaining-=w*frac
    return chosen,value,operations

def knapsack_dp(items,capacity):
    n=len(items); dp=[[0]*(capacity+1) for _ in range(n+1)]
    for i,(name,w,v) in enumerate(items,1):
        for c in range(capacity+1):
            if w<=c: dp[i][c]=max(dp[i-1][c],v+dp[i-1][c-w])
            else: dp[i][c]=dp[i-1][c]
    selected=[]; c=capacity
    for i in range(n,0,-1):
        if dp[i][c]!=dp[i-1][c]:
            name,w,v=items[i-1]; selected.append((name,w,v)); c-=w
    selected.reverse()
    return selected,dp[n][capacity],dp

def show(items,cap):
    print("Items (ID, weight, value):",items,"capacity=",cap)
    f,fv,ops=fractional(items,cap)
    print("Fractional greedy decisions:")
    for x in f: print(f"  {x[0]} fraction={x[1]:.2f} weight={x[2]:.2f} value={x[3]:.2f} ratio={x[4]:.2f}")
    print("Fractional value:",fv,"iterations:",ops)
    s,sv,dp=knapsack_dp(items,cap)
    print("0/1 DP selected:",s,"value:",sv,"DP states:",(len(items)+1)*(cap+1))
    print("DP final row:",dp[-1])
    # ratio-greedy 0/1 counterexample
    sorted_items=sorted(items,key=lambda x:x[2]/x[1],reverse=True)
    rem=cap; gs=[]; gv=0
    for name,w,v in sorted_items:
        if w<=rem: gs.append((name,w,v)); rem-=w; gv+=v
    print("0/1 ratio greedy:",gs,"value:",gv,"first commitment:",gs[0] if gs else None)

if __name__=="__main__":
    print("NORMAL INSTANCE")
    show([("A",10,60),("B",20,100),("C",30,120)],50)
    print("\nGREEDY COUNTEREXAMPLE")
    show([("A",10,60),("B",20,100),("C",30,120)],50)
    print("\nBOUNDARY capacity=0")
    show([("X",1,10)],0)
