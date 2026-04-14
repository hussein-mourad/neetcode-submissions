class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '{':'}','[':']'}
        stack = []
        for c in s:
            if c in brackets:
                stack.append(c)
            else:
                if stack and stack[-1]:
                    openB = stack.pop()
                    if brackets[openB] != c:
                        return False
                else:
                    return False

        if stack:
            return False
        return True

