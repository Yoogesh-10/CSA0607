# TOPIC 4 : DYNAMIC PROGRAMMING

**TOPIC 4 : DYNAMIC PROGRAMMING**

1. You are given the number of sides on a die (num_sides), the number of dice to throw (num_dice), and a target sum (target). Develop a program that utilizes dynamic programming to solve the Dice Throw Problem.

Test Cases:

1.Simple Case:

•Number of sides: 6

•Number of dice: 2

•Target sum: 7

2.More Complex Case:

•Number of sides: 4

•Number of dice: 3

•Target sum: 10

Output 

Test Case 1:

Number of ways to reach sum 7: 6

Test Case 2:

Number of ways to reach sum 10: 27



48.In a factory, there are two assembly lines, each with n stations. Each station performs a specific task and takes a certain amount of time to complete. The task must go through each station in order, and there is also a transfer time for switching from one line to another. Given the time taken at each station on both lines and the transfer time between the lines, the goal is to find the minimum time required to process a product from start to end.

Input

n: Number of stations on each line.

a1[i]: Time taken at station i on assembly line 1.

a2[i]: Time taken at station i on assembly line 2.

t1[i]: Transfer time from assembly line 1 to assembly line 2 after station i.

t2[i]: Transfer time from assembly line 2 to assembly line 1 after station i.

e1: Entry time to assembly line 1.

e2: Entry time to assembly line 2.

x1: Exit time from assembly line 1.

x2: Exit time from assembly line 2.

Output

The minimum time required to process the product.



49\.	An automotive company has three assembly lines (Line 1, Line 2, Line 3) to produce different car models. Each line has a series of stations, and each station takes a certain amount of time to complete its task. Additionally, there are transfer times between lines, and certain dependencies must be respected due to the sequential nature of some tasks. Your goal is to minimize the total production time by determining the optimal scheduling of tasks across these lines, considering the transfer times and dependencies.

Number of stations: 3

•  Station times:

•	Line 1: [5, 9, 3]

•	Line 2: [6, 8, 4]

•	Line 3: [7, 6, 5]

•  Transfer times:

[

  [0, 2, 3],

  [2, 0, 4],

  [3, 4, 0]

]

Dependencies: [(0, 1), (1, 2)] (i.e., the output of the first station is needed for the second, and the second for the third, regardless of the line).

50\.	 Write a c program to find the minimum path distance by using matrix form.

      	Test Cases: 

1\)	 

{0,10,15,20}

{10,0,35,25}

{15,35,0,30}

{20,25,30,0}

Output: 80



2\)&#x9;

{0,10,10,10}

{10,0,10,10}

{10,10,0,10}

{10,10,10,0}

Output: 40



3\)&#x9;

{0,1,2,3}

{1,0,4,5}

{2,4,0,6}

{3,5,6,0}

Output: 12



51\.	 Assume you are solving the Traveling Salesperson Problem for 4 cities (A, B, C, D) with known distances between each pair of cities. Now, you need to add a fifth city (E) to the problem.

Test Cases

1\. Symmetric Distances

•	Description: All distances are symmetric (distance from A to B is the same as B to A).

Distances:

A-B: 10, A-C: 15, A-D: 20, A-E: 25 B-C: 35, B-D: 25, B-E: 30 C-D: 30, C-E: 20 D-E: 15

Expected Output: The shortest route and its total distance. For example, A -> B -> D -> E -> C -> A might be the shortest route depending on the given distances.



52\.	 Given a string s, return the longest palindromic substring in S. 

Example 1: 

Input: s = "babad" 

Output: "bab" Explanation: "aba" is also a valid answer. 

Example 2: 

Input: s = "cbbd" 

Output: "bb" 

Constraints: ● 1 <= s.length <= 1000 ● s consist of only digits and English letters.



53\.	Given a string s, find the length of the longest substring without repeating characters.

Example 1: Input: s = "abcabcbb" Output: 3 

Explanation: The answer is "abc", with the length of 3. 

Example 2: Input: s = "bbbbb" Output: 1 

Explanation: The answer is "b", with the length of 1. 

Example 3: Input: s = "pwwkew" Output: 3

Explanation: The answer is "wke", with the length of 3. 

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring. Constraints: ● 0 <= s.length <= 5 \* 104 ● s consists of English letters, digits, symbols and spaces.



54\.	Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]

Output: true

Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]

Output: true

Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".

Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]

Output: false



55\.	Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words.Consider the following dictionary { i, like, sam, sung, samsung, mobile, ice, cream, icecream, man, go, mango}

Input:  ilike

Output: Yes 

The string can be segmented as "i like".

Input:  ilikesamsung

Output: Yes The string can be segmented as "i like samsung" or "i like sam sung".

56\.	Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified. You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters. Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right. For the last line of text, it should be left-justified, and no extra space is inserted between words. A word is defined as a character sequence consisting of non-space characters only.  Each word's length is guaranteed to be greater than 0 and not exceed maxWidth. The input array words contains at least one word.

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16

Output:

[   "This    is    an",

   "example  of text",

   "justification.  "

]

Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16

Output:

[

  "What   must   be",

  "acknowledgment  ",

  "shall be        "

]

Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.

Note that the second line is also left-justified because it contains only one word.

57\.	Design a special dictionary that searches the words in it by a prefix and a suffix. Implement the WordFilter class: WordFilter(string[] words) Initializes the object with the words in the dictionary.f(string pref, string suff) Returns the index of the word in the dictionary, which has the prefix pref and the suffix suff. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.

Example 1:

Input

["WordFilter", "f"]

[[["apple"]], ["a", "e"]]

Output

[null, 0]

Explanation

WordFilter wordFilter = new WordFilter(["apple"]);

wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = "e".



58\.	Implement Floyd's Algorithm to find the shortest path between all pairs of cities. Display the distance matrix before and after applying the algorithm. Identify and print the shortest path

Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4

Output: 3

Explanation: The figure above describes the graph. 

The neighboring cities at a distanceThreshold = 4 for each city are:

City 0 -> [City 1, City 2] 

City 1 -> [City 0, City 2, City 3] 

City 2 -> [City 0, City 1, City 3] 

City 3 -> [City 1, City 2] 

Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.

Test cases :

a) You are given a small network of 4 cities connected by roads with the following distances:

    City 1 to City 2: 3

    City 1 to City 3: 8

    City 1 to City 4: -4

    City 2 to City 4: 1

    City 2 to City 3: 4

    City 3 to City 1: 2

    City 4 to City 3: -5

    City 4 to City 2: 6

     Implement Floyd's Algorithm to find the shortest path between all pairs of cities. Display the distance matrix before and after applying the algorithm. Identify and print the shortest path from City 1 to City 3.

Input as above

Output : City 1 to City 3 = -9 



b. Consider a network with 6 routers. The initial routing table is as follows:

    Router A to Router B: 1

    Router A to Router C: 5

    Router B to Router C: 2

    Router B to Router D: 1

    Router C to Router E: 3

    Router D to Router E: 1

    Router D to Router F: 6

    Router E to Router F: 2



59\.	Write a Program to implement Floyd's Algorithm to calculate the shortest paths between all pairs of routers.  Simulate a change where the link between Router B and Router D fails. Update the distance matrix accordingly.  Display the shortest path from Router A to Router F before and after the link failure.

Input as above

Output : Router A to Router F = 5



60\.	Implement Floyd's Algorithm to find the shortest path between all pairs of cities. Display the distance matrix before and after applying the algorithm. Identify and print the shortest path

Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2

Output: 0

Explanation: The figure above describes the graph. 

The neighboring cities at a distanceThreshold = 2 for each city are:

City 0 -> [City 1] 

City 1 -> [City 0, City 4] 

City 2 -> [City 3, City 4] 

City 3 -> [City 2, City 4]

City 4 -> [City 1, City 2, City 3] 

The city 0 has 1 neighboring city at a distanceThreshold = 2.



a) Test cases :

B to A 2

A TO C 3

C TO D 1

D TO A 6 

C TO B 7 

Find shortest path from C to A 

Output = 7 



b) Find shortest path from E to C

C TO A 2

A TO B 4

B TO C 1

B TO E 6

E TO A 1

A TO D 5

D TO E 2

E TO D 4

D TO C 1

C TO D 3

 Output : E to C = 5



61\.	Implement the Optimal Binary Search Tree algorithm for the keys A,B,C,D with frequencies 0.1,0.2,0.4,0.3 Write the code using any programming language to construct the OBST for the given keys and frequencies. Execute your code and display the resulting OBST and its cost. Print the cost and root  matrix. 

Input N =4, Keys = {A,B,C,D} Frequencies =  {01.02.,0.3,0.4}

Output : 1.7

Cost Table

&#x9;0	1	2	3	4

1	0	0.1	0.4	1.1	1.7

2		0	0.2	0.8	0.4

3			0	0.4	1.0

4				0	0.3

5					0

Root table

&#x9;1	2	3	4

1	1	2	3	3

2		2	3	3

3			3	3

4				4



a)	Test cases

Input:  keys[] = {10, 12}, freq[] = {34, 50}

Output = 118

b)	Input:  keys[] = {10, 12, 20}, freq[] = {34, 8, 50}

Output = 142



62\.	 Consider a set of keys 10,12,16,21 with frequencies 4,2,6,3 and the respective probabilities.  Write a Program to construct an OBST in a programming language of your choice. Execute your code and display the resulting OBST, its cost and root matrix.

Input N =4, Keys = {10,12,16,21} Frequencies =  {4,2,6,3}

Output : 26

&#x9;0	1	2	3

0	4	80	202	262

1		2	102	162

2			6	12

3				3

a) Test cases

Input:  keys[] = {10, 12}, freq[] = {34, 50}

Output = 118

b) Input:  keys[] = {10, 12, 20}, freq[] = {34, 8, 50}

Output = 142



63\.	A game on an undirected graph is played by two players, Mouse and Cat, who alternate turns. The graph is given as follows: graph[a] is a list of all nodes b such that ab is an edge of the graph. The mouse starts at node 1 and goes first, the cat starts at node 2 and goes second, and there is a hole at node 0. During each player's turn, they must travel along one edge of the graph that meets where they are.  For example, if the Mouse is at node 1, it must travel to any node in graph[1]. Additionally, it is not allowed for the Cat to travel to the Hole (node 0).Then, the game can end in three ways:

If ever the Cat occupies the same node as the Mouse, the Cat wins.

If ever the Mouse reaches the Hole, the Mouse wins.

If ever a position is repeated (i.e., the players are in the same position as a previous turn, and it is the same player's turn to move), the game is a draw.

Given a graph, and assuming both players play optimally, return

1 if the mouse wins the game,

2 if the cat wins the game, or

0 if the game is a draw.

Example 1:

Input: graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]

Output: 0

Example 2:

Input: graph = [[1,3],[0],[3],[0,2]]

Output: 1



64\.	You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i]. Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability. If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

Example 1:

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2

Output: 0.25000

Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 \* 0.5 = 0.25.

Example 2:

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2

Output: 0.30000



65\.	There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time. Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner. The test cases are generated so that the answer will be less than or equal to 2 \* 10 9.

Example 1:

START					&#x9;

FINISH

Input: m = 3, n = 7

Output: 28

Example 2:

Input: m = 3, n = 2

Output: 3

Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:

1\. Right -> Down -> Down

2\. Down -> Down -> Right

3\. Down -> Right -> Down



66\.	Given an array of integers nums, return the number of good pairs. A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example 1:

Input: nums = [1,2,3,1,1,3]

Output: 4

Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:

Input: nums = [1,1,1,1]

Output: 6

Explanation: Each pair in the array are good.



67\.	There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold. Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number. Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

**Example 1:&#xA0;**

Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4

Output: 3

Explanation: The figure above describes the graph. 

The neighboring cities at a distanceThreshold = 4 for each city are:

City 0 -> [City 1, City 2] 

City 1 -> [City 0, City 2, City 3] 

City 2 -> [City 0, City 1, City 3] 

City 3 -> [City 1, City 2] 

Cities 0 and 3 have 2 neighboring cities at a distance Threshold = 4, but we have to return city 3 since it has the greatest number.

**Example 2:**

Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distance Threshold = 2

Output: 0

Explanation: The figure above describes the graph. 

The neighboring cities at a distance Threshold = 2 for each city are:

City 0 -> [City 1] 

City 1 -> [City 0, City 4] 

City 2 -> [City 3, City 4] 

City 3 -> [City 2, City 4]

City 4 -> [City 1, City 2, City 3] 

The city 0 has 1 neighboring city at a distanceThreshold = 2.





68\.	You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target. We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2

Output: 2

Example 2:

Input: times = [[1,2,1]], n = 2, k = 1

Output: 1

Example 3:

Input: times = [[1,2,1]], n = 2, k = 2

Output: -1
