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
                if not len(stack):
                    return False
                openB = stack.pop()
                if brackets[openB] != c:
                    return False
        if len(stack):
            return False
        return True

