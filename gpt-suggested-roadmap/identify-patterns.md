# 📘 DSA Patterns — Explanations + Examples

Below is a clean explanation of every major DSA pattern with simple examples showing **when** to use each pattern.

---

## 1. Sliding Window
Used for subarrays/substrings where the window **expands and shrinks** dynamically.

**When to use:**  
- Longest/shortest substring  
- At most K distinct chars  
- Subarray sum ≤ K  
- Fixed-size windows  

**Example:**  
Find the longest substring without repeating characters.

---

## 2. Two Pointers
Use two indices moving through the array to eliminate nested loops.

**When to use:**  
- Sorted arrays  
- Opposite-direction scanning  
- String/array comparisons  

**Example:**  
Check if a string is a palindrome by moving one pointer from left and one from right.

---

## 3. Fast & Slow Pointers (Tortoise–Hare)
Two pointers move at different speeds.

**When to use:**  
- Detecting cycles  
- Finding middle of linked list  
- Checking loop in arrays  

**Example:**  
Detect cycle in a linked list using slow (1 step) and fast (2 steps) pointers.

---

## 4. Hashing / Frequency Maps
Use hash maps to count or track occurrences.

**When to use:**  
- Anagrams  
- Top K frequencies  
- Track seen elements  
- Prefix sum patterns  

**Example:**  
Check if two strings are anagrams by counting character frequencies.

---

## 5. Prefix Sum
Store cumulative sums to answer range queries quickly.

**When to use:**  
- Range sum queries  
- Subarrays with specific sum  
- Differences between ranges  

**Example:**  
Count how many subarrays sum to `k` by using `prefix_sum[j] - prefix_sum[i] = k`.

---

## 6. Sorting + Greedy
Sort → make locally optimal choices to achieve a global optimum.

**When to use:**  
- Interval scheduling  
- Meeting rooms  
- Activity selection  
- Minimize/maximize cost  

**Example:**  
Merge intervals by sorting them first.

---

## 7. Binary Search / Binary Search on Answer
Search on a **sorted array** or on a **monotonically feasible answer**.

### A) Normal Binary Search  
Find element in sorted array.

### B) Binary Search on Answer  
Used when:  
"If I pick X, I can check if it's possible."

**Example:**  
Minimum capacity to ship packages in D days → binary search on capacity.

---

## 8. Binary Search Tree (BST) Patterns
Leverage the property:  
**left < root < right**

**When to use:**  
- kth smallest/largest  
- range queries  
- tree validation  

**Example:**  
Inorder traversal of a BST gives sorted order.

---

## 9. Bit Manipulation
Use bitwise operations for speed.

**When to use:**  
- Finding unique element  
- Creating subsets  
- Counting bits  

**Example:**  
Find the number that appears once when all others appear twice using XOR.

---

## 10. Backtracking
Try → explore → undo → try next.

**When to use:**  
- Generate combinations  
- Generate permutations  
- Solve N-queens  
- Solve subsets  

**Example:**  
Generate all subsets by choosing or not choosing each element.

---

## 11. Dynamic Programming (DP)

### A) 0/1 Knapsack  
Choose items once (take/not take).

**Example:**  
Subset sum → can we reach a target using elements?

### B) Unbounded Knapsack  
Take items unlimited times.

**Example:**  
Coin Change (minimum coins to make amount).

### C) Subsequence DP  
Comparing sequences.

**Example:**  
LCS – longest common subsequence.

### D) DP on Strings  
Usually involves palindromes.

**Example:**  
Longest palindromic substring.

### E) DP on Grids  
Path problems in a grid.

**Example:**  
Unique Paths (right/down moves only).

---

## 12. Matrix / Grid DFS-BFS
2D grid treated as a graph.

**When to use:**  
- Islands  
- Flood fill  
- Contamination spread  

**Example:**  
Count the number of islands by using DFS on connected components.

---

## 13. Graph BFS/DFS
Graphs represented with adjacency lists.

**When to use:**  
- Graph traversal  
- Connected components  
- Cycle detection  
- Shortest unweighted path  

**Example:**  
Use BFS to find shortest path in an unweighted graph.

---

## 14. Topological Sort
Produces ordering of tasks with dependencies.

**When to use:**  
- Course schedule problems  
- Build order  
- DAG dependencies  

**Example:**  
Given course prerequisites, find a valid order to take courses.

---

## 15. Shortest Path Algorithms

### Dijkstra — positive weights  
Find shortest path using min-heap.

### Bellman–Ford — negative weights allowed  
Detect negative cycles.

### Floyd–Warshall — all-pairs  
Compute all shortest paths.

**Example:**  
Network delay time using Dijkstra.

---

## 16. Union-Find (Disjoint Set)
Efficient structure to union groups and query connectivity.

**When to use:**  
- Find connected components  
- Cycle detection in graphs  
- Kruskal’s MST  
- Group merging  

**Example:**  
Accounts merge using Union-Find.

---

## 17. Tree DFS/BFS
Recursion-based divide-and-conquer for binary trees.

**When to use:**  
- Depth  
- Diameter  
- Path sum  
- LCA  

**Example:**  
Compute max depth of a tree using DFS.

---

## 18. Trie (Prefix Tree)
Tree where each node is a character.  

**When to use:**  
- Autocomplete  
- Word dictionary  
- Prefix search  
- Word search puzzles  

**Example:**  
Insert and search for words efficiently by character paths.

