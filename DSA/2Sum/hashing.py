class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        n = len(nums)
        for i in range(n):
            y=target-nums[i]
            
            if y in hash_map:
                return [hash_map[y], i]
            
            hash_map[nums[i]] = i
        
        return [0,0]
            