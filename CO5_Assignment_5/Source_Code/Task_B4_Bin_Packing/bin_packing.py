def first_fit_decreasing(items,capacity):
    bins=[]
    for item in sorted(items,reverse=True):
        for b in bins:
            if sum(b)+item<=capacity:
                b.append(item); break
        else:
            bins.append([item])
    return bins
def exact_min_bins(items,capacity):
    ordered=sorted(items,reverse=True)
    bins=[]
    best=len(items)
    def place(i):
        nonlocal best
        if i==len(ordered):
            best=min(best,len(bins)); return
        if len(bins)>=best:return
        x=ordered[i]; seen=set()
        for b in bins:
            rem=capacity-sum(b)
            if rem>=x and rem not in seen:
                seen.add(rem);b.append(x);place(i+1);b.pop()
        bins.append([x]);place(i+1);bins.pop()
    place(0)
    return best
def print_result(name,items,capacity):
    bins=first_fit_decreasing(items,capacity)
    print("\\n",name,"Items:",items,"Capacity:",capacity)
    for i,b in enumerate(bins,1):
        print(f"Server {i}: {b} | used={sum(b)} | remaining={capacity-sum(b)}")
    print("FFD servers:",len(bins))
    if len(items)<=12:
        print("Exact optimum:",exact_min_bins(items,capacity))
print_result("Normal case",[7,6,5,4,3,2,2,1],10)
print_result("Counterexample",[6,5,3,2,2,2],10)
print("\\nHeuristic: First-Fit Decreasing (FFD): sort descending; place in first server with room.")
print("Counterexample: FFD uses 3 servers, while exact packing uses 2 (6+2+2 and 5+3+2).")
print("FFD is practical but not guaranteed optimal.")
