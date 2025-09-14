# Problem no. 56

class Solution:
    def mergeSolution(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda i: i[0])
        output = intervals[0]

        for start, end in intervals[1:]:
            last_end = output[-1][1]

            if start <= end[-1][1]:
                output[-1][1] = max(last_end, end)
            else:
                output.append([start],[end])
        return output

# Time Complexity: O(N logn)