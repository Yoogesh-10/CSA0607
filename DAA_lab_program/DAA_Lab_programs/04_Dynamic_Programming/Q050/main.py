# DAA Assignment - Question 50
# Topic: Dynamic Programming
# Algorithm: House robber circular
# Time complexity: O(n)

def rob_line(a):
 p2=p1=0
 for x in a:p2,p1=p1,max(p1,p2+x)
 return p1
def rob_circle(a):
 return max(a[0],rob_line(a[1:]),rob_line(a[:-1])) if len(a)>1 else (a[0] if a else 0)
print("Maximum:",rob_circle([2,3,2]))
