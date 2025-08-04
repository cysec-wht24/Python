def longestSubarray(nums, k):
    n = len(nums) # gets number of elements in array
    max_length = 0 # initialization
    for i in range(n): # first iteration for loop, i is index
        total = 0 
        for j in range(i, n):
            total += nums[j]
            if total == k:
                max_length = max(max_length, j - i + 1)
    return max_length
                    

nums = [-3, 2, 1]
k=6
# Output: 0
ans = longestSubarray(nums, k)
print(ans)

# non-contiguous elements, that’s called a subsequence, not a subarray.
# subarray = contigious, meaning no gaps, no skipping.

# for i, num in enumerate(nums): # using both index and element
#     print(i, num)  # i is index, num is element

# for num in nums: # using only elements
#     print(num)  # this is the element