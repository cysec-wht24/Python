# Goal: Find Longest Subarray with sum K | Input Array: [Postives and Negatives]
from typing import List

def getLongestSubarray(a: List[int], k: int) -> int:
    n = len(a) # 5
    preSumMap = {} # [1]->0, [3]->1, [6]->2, [4]->3, [9]->4
    Sum = 0
    maxLen = 0 # 0, 0, 0, 2, 
    for i in range(n): # 0, 1, 2, 3, 4
        # calculate the prefix sum till index i:
        Sum += a[i] # 1, [1+2] = 3, [3+3]=6, [6+(-2)]=4, [4+5]=9
        # if the sum = k, update the maxLen:
        
        if Sum == k: # False, False, False, False, False
            maxLen = max(maxLen, i + 1)
        # a = [1, 2, 3, -2, 5]
        # k = 5
        # calculate the sum of remaining part i.e. x-k:

        rem = Sum - k # -4, [3-5] = -2, [6-5]=1, [4-5]=-1, [9-5]=4
        # Calculate the length and update maxLen:
        
        if rem in preSumMap: # [[r], [(key, value)], bool] = [-4, [], false], [-2, [(1:0)], false], [1, [(1:0),(3:1)], true], [-1, [(1:0),(3:1),(6:2)], false], [4, [(1:0),(3:1),(6:2),(4,3)], true]  
        # if there is a key=rem inside preSumMap
            length = i - preSumMap[rem] # (2-0)=2, (4-3)=1
            maxLen = max(maxLen, length) # 2, As 2> 1, thus maxLen = 2
        # Finally, update the map checking the conditions:
        
        if Sum not in preSumMap:
            preSumMap[Sum] = i # you saw Sum first time at index i
    return maxLen


# ✅ With if __name__ == "__main__": → behaves like a clean library
# Only run the code inside this block if this file is being run 
# directly (not imported by another file).
# ❌ Without it → behaves like a noisy script that always runs when imported
# all your function calls and print() statements will run automatically, 
# even though they were just trying to import your function.
# This is bad practice and causes unexpected side effects.

if __name__ == "__main__":
    a = [1, 2, 3, -2, 5]
    k = 5
    length = getLongestSubarray(a, k)
    print(f"The length of the longest subarray is: {length}")

# So we store the sum in hashmap, and we calculate the rem, if that rem 
# occurs in the hashmap (which is a group of summations) then we know 
# that we are currently operating on a group of subarrays in which one 
# of the subarray has the target summation and we can calculate the 
# indexes of that subarray by simply looking at the hashmap where the 
# summation happened and we can do that cause hashmap stores 
# key:  value and right now it is Sum: index it occured at so say that 
# index be j now the subarray index start from j+1 to i and done we have 
# found the subarray