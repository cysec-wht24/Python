def linearSearch(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
        
value = [2, 3, 4, 5, 3]
target = 3
ans = linearSearch(value, target)
print(ans)