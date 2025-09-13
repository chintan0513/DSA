# Problem no. 704

def binarySearch(nums: list[int], target: int) -> int:
    
    left = 0
    right = len(nums) - 1

    while left <= right:
        median = (left + right) // 2

        if nums[median] > target:
            right = median - 1
        elif nums[median] < target:
            left = median + 1
        else: return median
    
    return -1
    

print(binarySearch([-1,0,1,2,3,4,5,6,7,8,9], 0))

# Complexities:
# - time: O(log n) 
# - space/memory: O(1)