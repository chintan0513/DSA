# problem no. 217

def findDuplicates(nums: list[int])-> bool:
    
    hashSet = set()
    
    for n in nums:
        if n in hashSet:
            return True
        hashSet.add(n)
    return False

print(findDuplicates([1,2,3,4,5,6,1]))
print(findDuplicates([1,2,3,4,5,6]))
# Time complexity: O(n)
# Space complexity : O(n) because we are leveraging the additional hashmap/hashset, up to the size of the array.