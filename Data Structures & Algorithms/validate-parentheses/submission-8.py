class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n - 1
        while l < r:
            openB, closeB = s[l], s[r]       
            if openB == '(' and closeB != ')':
                return False
            if openB == '{' and closeB != '}':
                return False
            if openB == '[' and closeB != ']':
                return False
            l += 1
            r -= 1
        return True