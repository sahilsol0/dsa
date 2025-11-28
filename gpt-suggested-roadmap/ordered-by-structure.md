# ⭐ ULTIMATE LEETCODE STUDY PLAN  
## By Data Structure + Patterns + Problems (Escaped Numbers)

---

# 🔵 **1. STACKS**

## What to Learn
- Basic stack operations  
- Parentheses matching  
- Monotonic stack  
- Min Stack  
- Stack-based DFS  

## Monotonic Stack Template
```python
stack = []
for i, val in enumerate(nums):
    while stack and nums[stack[-1]] < val:
        stack.pop()
    stack.append(i)
```

## LeetCode Problems

### ⭐ Easy
- 20\. Valid Parentheses  
- 155\. Min Stack  
- 232\. Implement Queue Using Stacks  

### ⭐ Medium
- 739\. Daily Temperatures  
- 901\. Online Stock Span  
- 503\. Next Greater Element II  
- 150\. Evaluate Reverse Polish Notation  

### ⭐ Hard
- 84\. Largest Rectangle in Histogram  
- 85\. Maximal Rectangle  

---

# 🔵 **2. QUEUES & DEQUES**

## What to Learn
- BFS  
- Sliding Window (Monotonic Deque)  
- Multi-source BFS  
- Priority queue  

## BFS Template
```python
from collections import deque
q = deque([start])
visited = {start}

while q:
    node = q.popleft()
    for nei in graph[node]:
        if nei not in visited:
            visited.add(nei)
            q.append(nei)
```

## LeetCode Problems

### ⭐ Easy
- 933\. Number of Recent Calls  
- 225\. Implement Stack Using Queues  

### ⭐ Medium
- 102\. Binary Tree Level Order  
- 200\. Number of Islands  
- 994\. Rotting Oranges  
- 279\. Perfect Squares  
- 207\. Course Schedule  

### ⭐ Hard
- 239\. Sliding Window Maximum  
- 297\. Serialize and Deserialize Binary Tree  

---

# 🔵 **3. LINKED LISTS**

## What to Learn
- Two pointers  
- Reverse linked list  
- Detect cycle  
- Merge lists  
- Copy list with random pointer  

## Reverse List Template
```python
prev, cur = None, head
while cur:
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
return prev
```

## Detect Cycle Template
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True
return False
```

## LeetCode Problems

### ⭐ Easy
- 141\. Linked List Cycle  
- 206\. Reverse Linked List  

### ⭐ Medium
- 2\. Add Two Numbers  
- 19\. Remove Nth Node From End  
- 24\. Swap Nodes in Pairs  
- 138\. Copy List With Random Pointer  
- 148\. Sort List  

### ⭐ Hard
- 23\. Merge k Sorted Lists  

---

# 🔵 **4. HEAPS / PRIORITY QUEUE**

## What to Learn
- Min Heap  
- Max Heap with negation  
- Kth smallest/largest  
- Dijkstra  
- Merge K lists  

## Min-Heap Template
```python
import heapq
heapq.heappush(h, x)
heapq.heappop(h)
```

## Max-Heap Template
```python
heapq.heappush(h, -x)
val = -heapq.heappop(h)
```

## LeetCode Problems

### ⭐ Easy
- 703\. Kth Largest Element in a Stream  

### ⭐ Medium
- 215\. Kth Largest Element in an Array  
- 347\. Top K Frequent Elements  
- 973\. K Closest Points to Origin  
- 1438\. Longest Subarray With Limit  

### ⭐ Hard
- 23\. Merge k Sorted Lists  
- 295\. Find Median From Data Stream  

---

# 🔵 **5. BINARY TREES**

## What to Learn
- DFS (pre/in/post order)  
- BFS  
- Recursion  
- Construct tree  
- Lowest Common Ancestor  
- Tree views  

## DFS Template
```python
def dfs(node):
    if not node:
        return
    dfs(node.left)
    dfs(node.right)
```

## Level Order Template
```python
from collections import deque
q = deque([root])
while q:
    for _ in range(len(q)):
        node = q.popleft()
        ...
```

## LeetCode Problems

### ⭐ Easy
- 104\. Maximum Depth  
- 110\. Balanced Binary Tree  

### ⭐ Medium
- 102\. Level Order Traversal  
- 101\. Symmetric Tree  
- 114\. Flatten Binary Tree  
- 230\. Kth Smallest Element in BST  

### ⭐ Hard
- 124\. Binary Tree Maximum Path Sum  
- 297\. Serialize and Deserialize Binary Tree  

---

# 🔵 **6. GRAPHS**

## What to Learn
- DFS / BFS  
- Topological sort  
- Dijkstra  
- Union-Find  
- Grid graphs  
- Connected components  

## Grid BFS Template
```python
from collections import deque
q = deque([(r, c)])
visited = {(r, c)}

while q:
    r, c = q.popleft()
    for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        nr, nc = r+dr, c+dc
        if valid and (nr, nc) not in visited:
            visited.add((nr, nc))
            q.append((nr, nc))
```

## LeetCode Problems

### ⭐ Easy
- 733\. Flood Fill  
- 695\. Max Area of Island  

### ⭐ Medium
- 200\. Number of Islands  
- 207\. Course Schedule  
- 417\. Pacific Atlantic Water Flow  
- 994\. Rotting Oranges  
- 130\. Surrounded Regions  

### ⭐ Hard
- 127\. Word Ladder  
- 329\. Longest Increasing Path  
- 785\. Is Graph Bipartite?  

---

# 🔵 **7. TRIES**

## What to Learn
- Insert/search/startsWith  
- Word search  
- Dictionary problems  
- Prefix matching  

## Trie Template
```python
class TrieNode:
    def __init__(self):
        self.ch = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.ch:
                cur.ch[c] = TrieNode()
            cur = cur.ch[c]
        cur.end = True
```

## LeetCode Problems

### ⭐ Medium
- 208\. Implement Trie  
- 211\. Add and Search Word  
- 648\. Replace Words  
- 720\. Longest Word in Dictionary  

### ⭐ Hard
- 212\. Word Search II  
- 745\. Prefix and Suffix Search  

---

# 🔥 BONUS: HASHMAPS & SETS

## LeetCode Problems

### ⭐ Easy
- 1\. Two Sum  
- 242\. Valid Anagram  

### ⭐ Medium
- 3\. Longest Substring Without Repeating Characters  
- 49\. Group Anagrams  
- 560\. Subarray Sum Equals K  

### ⭐ Hard
- 30\. Substring with Concatenation of All Words  

