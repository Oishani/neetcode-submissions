"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i:i.start)
        
        for i in range(1, len(intervals)):
            i_prev = intervals[i - 1]
            i_current = intervals[i]

            if i_current.start < i_prev.end:
                return False
        return True

# Time: O(n log n) where n is number of intervals
# Space: O(n)
