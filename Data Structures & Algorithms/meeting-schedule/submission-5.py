"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key = lambda i: i.start)

        for i in range(1, len(intervals)):
            prev_meeting = intervals[i - 1]
            current_meeting = intervals[i]

            if prev_meeting.end > current_meeting.start:
                return False

        return True

# Time: O(n log n)
# Space: O(n)
