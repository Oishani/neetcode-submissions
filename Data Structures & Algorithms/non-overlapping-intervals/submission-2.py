class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i:i[0])
        prev_end = intervals[0][1]
        removed = 0

        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
            else:
                removed += 1
                prev_end = min(prev_end, end)
        return removed
        
# Time: O(n log n) where n is number of intervals
# Space: O(n)
        