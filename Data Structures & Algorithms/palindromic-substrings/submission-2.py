class Solution:
    def countSubstrings(self, s: str) -> int:
        # Initialize a counter to count palindromes.
        res = 0
        # Loop over every character in the string.
        for i in range(len(s)):
            # For detecting odd length palindromes, initialize a left and right pointer at the same position.
            l, r, = i, i
            # We're moving from middle out, so the left pointer needs to be greater than the first index, and 
            # the right pointer needs to be smaller than the length of the string.
            # While the pointers are within this range and the characters at each pointer are equal,
            while l >=0 and r < len(s) and s[l] == s[r]:
                # we have found a new palindrome, so increment the counter.
                res += 1
                # Move out the pointers.
                l -= 1
                r += 1

            # For detecting even length palindromes, initialize a left and right pointer at i and i + 1.
            l, r, = i, i + 1
            # We're moving from middle out, so the left pointer needs to be greater than the first index, and 
            # the right pointer needs to be smaller than the length of the string.
            # While the pointers are within this range and the characters at each pointer are equal,
            while l >=0 and r < len(s) and s[l] == s[r]:
                # we have found a new palindrome, so increment the counter.
                res += 1
                # Move out the pointers.
                l -= 1
                r += 1
        # Return the result.
        return res

# Time: O(n^2)
# Space: O(n)
