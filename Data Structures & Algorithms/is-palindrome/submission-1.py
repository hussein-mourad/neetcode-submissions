class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            c1, c2 = s[l].lower(), s[r].lower()
            if not c1.isalnum():
                l += 1
                continue
            if not c2.isalnum():
                r -= 1
                continue
            if c1 != c2:
                return False
            l += 1
            r -= 1
        return True