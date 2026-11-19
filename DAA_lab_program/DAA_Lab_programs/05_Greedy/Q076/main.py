# DAA Assignment - Question 76
# Topic: Greedy
# Algorithm: Interval partitioning
# Time complexity: O(n²)

def partition(intervals):
 rooms=[]
 for s,e in sorted(intervals):
  for i,(end,room) in enumerate(rooms):
   if end<=s:rooms[i]=(e,room);break
  else:rooms.append((e,len(rooms)+1))
 return len(rooms)
print("Rooms:",partition([(0,30),(5,10),(15,20)]))
