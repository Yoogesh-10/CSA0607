# DAA Assignment - Question 16
# Topic: Brute Force
# Algorithm: Three sum zero
# Time complexity: O(n³)

def three_sum(a):
    out=set()
    for i in range(len(a)):
      for j in range(i+1,len(a)):
       for k in range(j+1,len(a)):
        if a[i]+a[j]+a[k]==0:out.add(tuple(sorted((a[i],a[j],a[k]))))
    return sorted(out)
print(three_sum([-1,0,1,2,-1,-4]))
