from itertools import combinations
def exact_set_cover(zones, centers):
    best=None; states=0
    keys=list(centers)
    for r in range(1,len(keys)+1):
      for subset in combinations(keys,r):
        states+=1
        covered=set().union(*(centers[x] for x in subset))
        if covered>=zones:
          best=subset; return best,states
    return None,states
def greedy_set_cover(zones,centers):
    uncovered=set(zones); chosen=[]; steps=0
    while uncovered:
      candidates=[c for c in centers if c not in chosen]
      if not candidates: return None,steps
      c=max(candidates,key=lambda x:len(centers[x]&uncovered))
      gain=len(centers[c]&uncovered); steps+=1
      if gain==0:return None,steps
      chosen.append(c); uncovered-=centers[c]
    return chosen,steps
instances={
"1":({1,2,3,4},{'C1':{1,2},'C2':{3,4},'C3':{1,3},'C4':{2,4}}),
"2":({1,2,3,4,5},{'C1':{1,2,3},'C2':{3,4},'C3':{4,5},'C4':{1,5}}),
"3":({1,2,3,4,5,6},{'C1':{1,2,3,4},'C2':{1,2},'C3':{3,4},'C4':{5,6},'C5':{1,5},'C6':{2,6}}),
"Counterexample":({1,2,3,4,5,6},{'A':{1,2,3,4},'B':{1,2,5},'C':{3,4,6}})
}
for name,(z,c) in instances.items():
 print("\\nINSTANCE",name,"Zones:",sorted(z))
 exact,states=exact_set_cover(z,c); greedy,steps=greedy_set_cover(z,c)
 print("Centers:",{k:sorted(v) for k,v in c.items()})
 print("Exact:",exact,"size",len(exact) if exact else None,"combination states",states)
 print("Greedy:",greedy,"size",len(greedy) if greedy else None,"selection steps",steps)
 if name=="Counterexample":
  uncovered=set(z); trace=[]
  for chosen in greedy:
   gain=c[chosen]&uncovered; trace.append((chosen,sorted(gain))); uncovered-=gain
  print("Greedy trace:",trace)
