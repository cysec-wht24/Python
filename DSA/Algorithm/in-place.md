# 🔢 Sorting Algorithms

| Algorithm       | In-Place | Why?                                               |
|----------------|----------|----------------------------------------------------|
| Bubble Sort     | ✅        | Swaps are performed within the array              |
| Insertion Sort  | ✅        | Elements are shifted inside the same array        |
| Selection Sort  | ✅        | Swaps elements directly within the array          |
| Quick Sort      | ✅        | Can be implemented in-place using partitioning    |
| Heap Sort       | ✅        | Heap is built within the same array               |
| Shell Sort      | ✅        | Gaps are used to rearrange elements in-place      |

> 🔴 **Note:** Merge Sort is **not** in-place by default (uses O(n) extra space), though advanced versions can achieve in-place sorting with significant complexity.

---

# 📚 Array / List Manipulations

| Operation                        | In-Place | Notes                                         |
|----------------------------------|----------|-----------------------------------------------|
| Reversing an array               | ✅        | Swapping left and right elements              |
| Rotating an array (by k steps)   | ✅        | If done using the reversal algorithm          |
| Removing duplicates (sorted)     | ✅        | Overwrites duplicates with unique elements    |
| Moving zeroes to the end         | ✅        | Swaps zero and non-zero elements              |
| Partitioning (like QuickSort)    | ✅        | Swaps elements within the array               |
| Cyclic Sort                      | ✅        | Rearranges elements to correct positions      |

---

# 🔍 Search and Miscellaneous Algorithms

| Operation                              | In-Place | Notes                                       |
|----------------------------------------|----------|---------------------------------------------|
| Binary Search                          | ✅        | Uses only pointers or indexes               |
| Floyd’s Cycle Detection (Tortoise & Hare) | ✅     | Uses two pointers only                      |
| Matrix Transposition (square matrix)   | ✅        | Swaps elements matrix[i][j] with matrix[j][i]|
| Diagonal / Spiral Traversal            | ✅        | Doesn’t require extra matrix                |
| Reversing a linked list                | ✅        | Rewires the `.next` pointers                |

---

# 📐 In-Place Matrix Algorithms

| Operation               | In-Place | Notes                                           |
|------------------------|----------|-------------------------------------------------|
| Transpose matrix       | ✅        | For square matrices                            |
| Rotate matrix 90°      | ✅        | Transpose + reverse rows or columns            |
| Set Matrix Zeroes      | ✅        | If optimized, uses first row/column as markers |

---

# 🧠 Tip: What is In-Place?

**In-place** algorithms do **not** use additional data structures that grow with input size (like extra arrays or matrices).  
They typically use only a **constant number of extra variables**, keeping space complexity at **O(1)**.


