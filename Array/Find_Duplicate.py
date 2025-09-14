# problem no. 287

class Solution:
    def findDuplicateNum(self, nums: list[int])-> int :
        hashSet = set()

        for n in nums:
            if n in hashSet:
                return n
            hashSet.add(n)
        return
    
print(Solution().findDuplicateNum([1,2,3,4,5,6]))
print(Solution().findDuplicateNum([1,2,3,4,5,1]))

# time complexity : o(n)
# space complexity: o(n)