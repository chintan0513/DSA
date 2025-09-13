# Problem no. 387

from collections import defaultdict

class Solution:
    def firstUniqueChar(self, s: str) -> int:

        count = defaultdict(int)# need a hashmap

        for c in s:
            count[c] += 1
        
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1
    
print(Solution().firstUniqueChar('leetcode'))