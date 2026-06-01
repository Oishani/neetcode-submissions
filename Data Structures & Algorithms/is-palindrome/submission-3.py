class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize a left and right pointer at the first and last indices.
        l, r = 0, len(s) - 1

        # Run a while loop till l <=r.
        while l < r:
            while l < r and not self.alphanum(s[r]):
                r -= 1
            while l < r and not self.alphanum(s[l]):
                l += 1
            # The moment the characters (converted to lowercase) at the two pointers are unequal, return False.
            if s[l].lower() != s[r].lower():
                return False
            # Otherwise, keep moving the pointers inwards.
            l += 1
            r -= 1

        # At the end of the while loop completion, return True.
        return True

    # Define a function to return True if a character is alphanumeric.
    def alphanum(self, c):
        return (ord("A") <= ord(c) <= ord("Z")) or (ord("a") <= ord(c) <= ord("z")) or (ord("0") <= ord(c) <= ord("9"))