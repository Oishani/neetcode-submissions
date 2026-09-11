class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_index = {}
        for i, ch in enumerate(s):
            char_index[ch] = i

        result = []
        end = -1
        size = 0

        for i, ch in enumerate(s):
            end = max(end, char_index[ch])
            size += 1
            if i == end:
                result.append(size)
                size = 0
                end = -1
        return result

# Time: O(n) where n is len of string
# Space: O(n) = O(26) = O(1)

