# Task 4: Assembly Line Scheduling DP
def assembly(a1,a2,t,e,x):
    n=len(a1); f1=[0]*n;f2=[0]*n;back1=[0]*n;back2=[0]*n
    f1[0]=e[0]+a1[0];f2[0]=e[1]+a2[0]
    print("Station 1 costs:",f1[0],f2[0])
    for i in range(1,n):
        stay1=f1[i-1]+a1[i]; transfer1=f2[i-1]+t[1][i-1]+a1[i]
        stay2=f2[i-1]+a2[i]; transfer2=f1[i-1]+t[0][i-1]+a2[i]
        f1[i]=min(stay1,transfer1);back1[i]=0 if stay1<=transfer1 else 1
        f2[i]=min(stay2,transfer2);back2[i]=1 if stay2<=transfer2 else 0
        print(f"Station {i+1}: L1 stay={stay1} transfer={transfer1} choose={'stay' if back1[i]==0 else 'transfer'}; L2 stay={stay2} transfer={transfer2} choose={'stay' if back2[i]==1 else 'transfer'}")
    end1=f1[-1]+x[0];end2=f2[-1]+x[1]
    line=0 if end1<=end2 else 1
    cost=min(end1,end2);route=[line]
    for i in range(n-1,0,-1):route.append(back1[i] if route[-1]==0 else back2[i])
    route.reverse()
    return cost,route,f1,f2
def show(a1,a2,t,e,x):
    print("Line1:",a1,"Line2:",a2,"transfer:",t,"entry:",e,"exit:",x)
    cost,route,f1,f2=assembly(a1,a2,t,e,x)
    print("Route:",["Line "+str(k+1) for k in route],"transfer stations:",[i+1 for i in range(1,len(route)) if route[i]!=route[i-1]])
    print("Minimum time:",cost)
if __name__=="__main__":
    a1=[7,9,3,4,8,4];a2=[8,5,6,4,5,7]
    t=[[2,3,1,3,4],[2,1,2,2,1]]
    e=[2,4];x=[3,2]
    print("BASE CASE");show(a1,a2,t,e,x)
    print("\nTRANSFER CHANGE: t[Line1->Line2 at station 3] increased 1->20")
    t2=[row[:] for row in t];t2[0][2]=20;show(a1,a2,t2,e,x)
    print("\nDISRUPTION: Line 1 station 4 processing 4->30")
    a1b=a1[:];a1b[3]=30;show(a1b,a2,t,e,x)
    print("\nBOUNDARY: one station")
    show([5],[7],[[],[]],[0,0],[1,1])
