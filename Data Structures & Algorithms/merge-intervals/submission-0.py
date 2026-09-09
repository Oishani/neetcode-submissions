class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])

        result = [intervals[0]]

        for start, end in intervals[1:]:
            prev_end = result[-1][1]

            if start <= prev_end:
                result[-1][1] = max(prev_end, end)
            else:
                result.append([start, end])
        return result

        