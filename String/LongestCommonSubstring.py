# Problem no. 3

class Solution:
    def longestCommonSubStrng(self, s: str) -> int:
        
        charSet = set()
        l = 0           # left pointer
        res = 0 

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l +1)
        return res

print(Solution().longestCommonSubStrng('abcabcbb'))

# time complexity : O(n) because it visits each and every character or member in the string atleast once 
# space/ memory complexity: O(n)