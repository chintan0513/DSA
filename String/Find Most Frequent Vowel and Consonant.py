# Problem no. 3541

from collections import defaultdict

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = defaultdict(int)
        consonants = defaultdict(int)

        for x in s:
            if x in 'aeiou':
                vowels[x] += 1
            else:
                consonants[x] += 1

        return max(vowels.values() or [0]) + max(consonants.values() or [0])
