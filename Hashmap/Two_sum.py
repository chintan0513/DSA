from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # store val: index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return (prevMap[diff], i)
            else:
                prevMap[n] = i
        return

twoSum = Solution().twoSum
# test cases
print(twoSum([2,7,11,15], 9)) # [0,1]
print(twoSum([3,2,4], 6)) # [1,2]

# Time: O(n)
# Space: O(n)
# Hashmap

