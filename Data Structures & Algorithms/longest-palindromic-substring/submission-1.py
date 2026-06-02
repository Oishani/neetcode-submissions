class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Initialize an empty string that will hold the final result.
        res = ""
        # Initialize the length of the final string to be 0.
        res_len = 0

        # Loop over every character in the string.
        for i in range(len(s)):
            # For detecting odd length palindromes, initialize a left and right pointer at the same position.
            l, r, = i, i
            # We're moving from middle out, so the left pointer needs to be greater than the first index, and 
            # the right pointer needs to be smaller than the length of the string.
            # While the pointers are within this range and the characters at each pointer are equal,
            while l >=0 and r < len(s) and s[l] == s[r]:
                # we have found a new palindrome, so check if its length is greater than the current result length.
                if (r - l + 1) > res_len:
                    # If yes, update the result and it's length.
                    res = s[l:r + 1]
                    res_len = r - l + 1
                # Move out the pointers.
                l -= 1
                r += 1

            # For detecting even length palindromes, initialize a left and right pointer at i and i + 1.
            l, r, = i, i + 1
            # We're moving from middle out, so the left pointer needs to be greater than the first index, and 
            # the right pointer needs to be smaller than the length of the string.
            # While the pointers are within this range and the characters at each pointer are equal,
            while l >=0 and r < len(s) and s[l] == s[r]:
                # we have found a new palindrome, so check if its length is greater than the current result length.
                if (r - l + 1) > res_len:
                    # If yes, update the result and it's length.
                    res = s[l:r + 1]
                    res_len = r - l + 1
                # Move out the pointers.
                l -= 1
                r += 1
        # Return the result.
        return res

# Time: O(n^2)
# Space: O(n)
