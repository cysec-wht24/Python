class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        n = len(nums)
        
        left = 0
        right = n-1

        while left < right:
            a = 0
            a = nums[left] + nums[right]
            
            if a == target:
                return [left, right]
            
            if a < target:
                left+=1
            
            else:
                right-=1
        
        return [0,0]
    
    # Won't work in leetcode as it fucks the indexes for output