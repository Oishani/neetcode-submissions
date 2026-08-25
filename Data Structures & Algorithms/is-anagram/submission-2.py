class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = Counter(s)
        counter_t = Counter(t)

        return counter_s == counter_t

# Time: O(n + m) where n is len of s and m is len of t
# Space: O(n + m)
        