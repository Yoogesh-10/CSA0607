# DAA Assignment - Question 97
# Topic: Tractability and Approximation
# Algorithm: Hamiltonian path verifier
# Time complexity: Verification O(V+E)

def verify_path(g,path):
 return len(path)==len(g) and len(set(path))==len(path) and all(g[path[i]][path[i+1]] for i in range(len(path)-1))
g=[[0,1,0,0],[1,0,1,0],[0,1,0,1],[0,0,1,0]]
p=[0,1,2,3]
print("Path valid:",verify_path(g,p))
