# increament i till it lands on element greater than pivot 
# if found stop

# decrement j until you find a element smaller than or equal to pivot
# if found stop

# then interchange both i and j
# continue

# if i becomes greater than j then don't interchange i and j as we have found the pivot actual position
# Now  interchange j and pivot element

# Now we partition array into subarray based on the former pivot current fixed position, and perform quicksort on them
# This is an recursive algorithm

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choose middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return self.quick_sort(left) + middle + self.quick_sort(right)

# Example usage
arr = [5, 3, 8, 4, 2, 7, 1, 10]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)