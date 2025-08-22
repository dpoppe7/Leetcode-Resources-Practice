# BIG O COMPLEXITY CHART

## DATA STRUCTURES COMPLEXITY

### ARRAYS
## Definition: 
A collection of elements stored in contiguous memory locations.
## Time Complexity:

Access: O(1)
Search: O(n)
Insertion: O(n) (worst case), O(1) (end)
Deletion: O(n) (worst case), O(1) (end)

## Space Complexity: 
O(n)
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Access | O(1) no iteration | O(1) |
| Search - Linear (unsorted) | O(n) | O(1) |
| Search - Binary (sorted) | O(log n) | O(1) |
| Insert at end | O(1) no shifting | O(1) |
| Insert at index | O(n) shifting elemetns (right) | O(1) |
| Delete from end | O(1) no shifting | O(1) |
| Delete from index | O(n) shifting elements (left) | O(1) |
| Update | O(1) no shifting | O(1) |

### LINKED LISTS
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Access | O(n) | O(1) |
| Search | O(n) | O(1) |
| Insert at head | O(1) | O(1) |
| Insert at tail | O(1)* / O(n) | O(1) |
| Insert at index | O(n) | O(1) |
| Delete at head | O(1) | O(1) |
| Delete at tail | O(1)* / O(n) | O(1) |
| Delete at index | O(n) | O(1) |

*O(1) if tail pointer available

### STACKS
## Definition: 
A Last-In-First-Out (LIFO) data structure where elements are added and removed from the same end (top).

## Time Complexity:

Time depends on how you implement it. It's ok to implement as Dynamic arrays

Push: O(1)
Pop: O(1)
Peek/Top: O(1)
Search: O(n)

## Space Complexity: 
O(n)

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Push/append | O*(1) | O(1) |
| Pop | O(1) | O(1) |
| Peek/Top | O(1) | O(1) |
| isEmpty | O(1) | O(1) |
| Search | O(n) | O(1) |

*on average

### QUEUES
## Definition
A First-In-First-Out (FIFO) data structure where elements are added at the rear and removed from the front.

## Time Complexity:

Probably implemented as a double-linked list.
Enqueue: O(1) an append operation 
Dequeue: O(1) ' Pop'
Front: O(1)
Search: O(n)

## Space Complexity: 
O(n)

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Enqueue | O(1) | O(1) |
| Dequeue | O(1) | O(1) |
| Front | O(1) | O(1) |
| isEmpty | O(1) | O(1) |
| Search | O(n) | O(1) |

### HASH TABLES
| Operation | Average Case | Worst Case | Space Complexity |
|-----------|-------------|------------|------------------|
| Insert | O(1) | O(n) | O(n) |
| Delete | O(1) | O(n) | O(1) |
| Search | O(1) | O(n) | O(1) |
| Update | O(1) | O(n) | O(1) |

### BINARY SEARCH TREES
| Operation | Average Case | Worst Case | Space Complexity |
|-----------|-------------|------------|------------------|
| Search | O(log n) | O(n) | O(1) |
| Insert | O(log n) | O(n) | O(1) |
| Delete | O(log n) | O(n) | O(1) |
| Find Min/Max | O(log n) | O(n) | O(1) |
| In-order Traversal | O(n) | O(n) | O(h) |

### BALANCED BST (AVL, Red-Black)
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Search | O(log n) | O(1) |
| Insert | O(log n) | O(1) |
| Delete | O(log n) | O(1) |
| Find Min/Max | O(log n) | O(1) |

### HEAPS
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Insert | O(log n) | O(1) |
| Extract Min/Max | O(log n) | O(1) |
| Peek | O(1) | O(1) |
| Build Heap | O(n) | O(1) |
| Heapify | O(log n) | O(1) |

### TRIE
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Insert | O(m) | O(m) |
| Search | O(m) | O(1) |
| Delete | O(m) | O(1) |
| Prefix Search | O(p) | O(1) |
| Space (overall) | - | O(ALPHABET_SIZE × N × M) |

*m = word length, p = prefix length, N = number of words, M = average word length

### UNION FIND (Disjoint Set)
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Find | O(α(n)) | O(1) |
| Union | O(α(n)) | O(1) |
| Connected | O(α(n)) | O(1) |
| Space (overall) | - | O(n) |

*α(n) = inverse Ackermann function (practically constant)

---

## SORTING ALGORITHMS COMPLEXITY

| Algorithm | Best Case | Average Case | Worst Case | Space | Stable |
|-----------|----------|-------------|------------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting Sort | O(n + k) | O(n + k) | O(n + k) | O(k) | Yes |
| Radix Sort | O(d × n) | O(d × n) | O(d × n) | O(n + k) | Yes |

*k = range of input, d = number of digits

---

## SEARCHING ALGORITHMS COMPLEXITY

| Algorithm | Time Complexity | Space Complexity | Requirements |
|-----------|----------------|------------------|--------------|
| Linear Search | O(n) | O(1) | None |
| Binary Search | O(log n) | O(1) | Sorted array |
| Hash Table Search | O(1) avg, O(n) worst | O(n) | Hash function |
| BST Search | O(log n) avg, O(n) worst | O(1) | BST structure |

---

## GRAPH ALGORITHMS COMPLEXITY

| Algorithm | Time Complexity | Space Complexity | Use Case |
|-----------|----------------|------------------|----------|
| DFS | O(V + E) | O(V) | Traversal, Cycle detection |
| BFS | O(V + E) | O(V) | Shortest path (unweighted) |
| Dijkstra | O(V²) or O(E log V) | O(V) | Shortest path (non-negative) |
| Bellman-Ford | O(VE) | O(V) | Shortest path (negative edges) |
| Floyd-Warshall | O(V³) | O(V²) | All pairs shortest path |
| Kruskal's MST | O(E log E) | O(V) | Minimum spanning tree |
| Prim's MST | O(E log V) | O(V) | Minimum spanning tree |
| Topological Sort | O(V + E) | O(V) | DAG ordering |

*V = vertices, E = edges

---

## TREE TRAVERSAL COMPLEXITY

| Traversal | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| In-order | O(n) | O(h) |
| Pre-order | O(n) | O(h) |
| Post-order | O(n) | O(h) |
| Level-order (BFS) | O(n) | O(w) |

*h = height of tree, w = maximum width of tree

---

## PROBLEM SOLVING PATTERNS COMPLEXITY

### TWO POINTERS
| Pattern | Time Complexity | Space Complexity |
|---------|----------------|------------------|
| Opposite Direction | O(n) | O(1) |
| Same Direction | O(n) | O(1) |
| Fast & Slow | O(n) | O(1) |

### SLIDING WINDOW
| Pattern | Time Complexity | Space Complexity |
|---------|----------------|------------------|
| Fixed Size | O(n) | O(1) |
| Variable Size | O(n) | O(1) |

### PREFIX SUM
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Build Prefix Array | O(n) | O(n) |
| Range Query | O(1) | O(1) |
| 2D Prefix Sum Build | O(mn) | O(mn) |
| 2D Range Query | O(1) | O(1) |

### DIVIDE AND CONQUER
| Problem Type | Time Complexity | Space Complexity |
|-------------|----------------|------------------|
| Binary Division | O(n log n) | O(log n) |
| Master Theorem T(n) = aT(n/b) + f(n) | Depends on a,b,f(n) | O(log n) |

### DYNAMIC PROGRAMMING
| Pattern | Time Complexity | Space Complexity |
|---------|----------------|------------------|
| 1D DP | O(n) | O(n) or O(1) |
| 2D DP | O(mn) | O(mn) or O(m) |
| Top-down (Memoization) | O(states × work_per_state) | O(states) |
| Bottom-up (Tabulation) | O(states × work_per_state) | O(states) |

### BACKTRACKING
| Problem Type | Time Complexity | Space Complexity |
|-------------|----------------|------------------|
| Permutations | O(n! × n) | O(n) |
| Combinations | O(2ⁿ × n) | O(n) |
| N-Queens | O(n!) | O(n) |
| Sudoku | O(9^(n²)) | O(n²) |

### TOP K ELEMENTS
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Min/Max Heap | O(n log k) | O(k) |
| Quick Select | O(n) avg, O(n²) worst | O(1) |
| Sorting | O(n log n) | O(1) or O(n) |

---

## COMPLEXITY GROWTH RATES (Best to Worst)

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Hash table lookup |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Linear search |
| O(n log n) | Linearithmic | Merge sort |
| O(n²) | Quadratic | Bubble sort |
| O(n³) | Cubic | Floyd-Warshall |
| O(2ⁿ) | Exponential | Fibonacci (naive) |
| O(n!) | Factorial | Traveling salesman (brute force) |