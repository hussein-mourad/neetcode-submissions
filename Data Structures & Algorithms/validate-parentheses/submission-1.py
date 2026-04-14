class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '{':'}','[':']'}
        openBrackets = ['(','{','[']
        closeBrackets = [')','}',']']
        stack = []
        for c in s:
            if c in openBrackets:
                stack.append(c)
            elif c in closeBrackets:
                openB = stack.pop()
                if brackets[openB] != c:
                    return False
        return True

