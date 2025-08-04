def unionArray(nums1, nums2):
        setis = set(nums1 + nums2)
        return list(setis)

nums1 = [3, 4, 6, 7, 9, 9]
nums2 = [1, 5, 7, 8, 8]
# Output: [1, 3, 4, 5, 6, 7, 8, 9]
# could use map or pointer
ans = unionArray(nums1, nums2)
print(ans) 