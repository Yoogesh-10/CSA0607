# TOPIC 7:

TOPIC 7:TRACTABILITY AND APPROXIMATION ALGORITHM

97.Implement a program to verify if a given problem is in class P or NP. Choose a specific decision problem (e.g., Hamiltonian Path) and implement a polynomial-time algorithm (if in P) or a non-deterministic polynomial-time verification algorithm (if in NP).

**Input:**

- Graph G with vertices V = {A, B, C, D} and edges E = {(A, B), (B, C), (C, D), (D, A)}

**Output:**

- Hamiltonian Path Exists: True (Path: A -> B -> C -> D)



98.Implement a solution to the 3-SAT problem and verify its NP-Completeness. Use a known NP-Complete problem (e.g., Vertex Cover) to reduce it to the 3-SAT problem.

**Input:**

- 3-SAT Formula: (x1 ∨ x2 ∨ ¬x3) ∧ (¬x1 ∨ x2 ∨ x4) ∧ (x3 ∨ ¬x4 ∨ x5)
- Reduction from Vertex Cover: Vertex Cover instance with V = {1, 2, 3, 4, 5}, E = {(1,2), (1,3), (2,3), (3,4), (4,5)}

**Output:**

- Satisfiability: True (Example satisfying assignment: x1 = True, x2 = True, x3 = False, x4 = True, x5 = False)
- NP-Completeness Verification: Reduction successful from Vertex Cover to 3-SAT



99.Implement an approximation algorithm for the Vertex Cover problem. Compare the performance of the approximation algorithm with the exact solution obtained through brute-force. Consider the following graph G=(V,E) where V={1,2,3,4,5} and E={(1,2),(1,3),(2,3),(3,4),(4,5).

**Input:**

- Graph G = (V, E) with V = {1, 2, 3, 4, 5}, E = {(1,2), (1,3), (2,3), (3,4), (4,5)}

**Output:**

- Approximation Vertex Cover: {2, 3, 4}
- Exact Vertex Cover (Brute-Force): {2, 4}
- Performance Comparison: Approximation solution is within a factor of 1.5 of the optimal solution.



100.Implement a greedy approximation algorithm for the Set Cover problem. Analyze its performance on different input sizes and compare it with the optimal solution. Consider the following universe U={1,2,3,4,5,6,7} and sets ={{1,2,3},{2,4},{3,4,5,6},{4,5},{5,6,7},{6,7}}

**Input:**

- Universe U = {1, 2, 3, 4, 5, 6, 7}
- Sets S = {{1, 2, 3}, {2, 4}, {3, 4, 5, 6}, {4, 5}, {5, 6, 7}, {6, 7}}

**Output:**

- Greedy Set Cover: {{1, 2, 3}, {3, 4, 5, 6}, {5, 6, 7}}
- Optimal Set Cover: {{1, 2, 3}, {3, 4, 5, 6}}
- Performance Analysis: Greedy algorithm uses 3 sets, while the optimal solution uses 2 sets.



101.Implement a heuristic algorithm (e.g., First-Fit, Best-Fit) for the Bin Packing problem. Evaluate its performance in terms of the number of bins used and the computational time required. Consider a list of item weights {4,8,1,4,2,1}and a bin capacity of 10.

**Input:**

- List of item weights: {4, 8, 1, 4, 2, 1}
- Bin capacity: 10

**Output:**

- Number of Bins Used: 3
- Bin Packing: Bin 1: [4, 4, 2], Bin 2: [8, 1, 1], Bin 3: [1]
- Computational Time: O(n)



102.Implement an approximation algorithm for the Maximum Cut problem using a greedy or randomized approach. Compare the results with the optimal solution obtained through an exhaustive search for small graph instances. 

**Input:**

- Graph G = (V, E) with V = {1, 2, 3, 4}, E = {(1,2), (1,3), (2,3), (2,4), (3,4)}
- Edge Weights: w(1,2) = 2, w(1,3) = 1, w(2,3) = 3, w(2,4) = 4, w(3,4) = 2

**Output:**

- Greedy Maximum Cut: Cut = {(1,2), (2,4)}, Weight = 6
- Optimal Maximum Cut (Exhaustive Search): Cut = {(1,2), (2,4), (3,4)}, Weight = 8
- Performance Comparison: Greedy solution achieves 75% of the optimal weight.
