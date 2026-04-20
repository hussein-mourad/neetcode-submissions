class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        res = 0
        for token in tokens:
            if token in operators:
                r =  stack.pop()
                l = stack.pop()
                res = self.eval_expr(int(l), int(r), token)
                stack.append(res)
            else:
                stack.append(token)
        if len(tokens) == 1:
            return int(tokens[0])
        return res
             
    def eval_expr(self,l: str, r: str, operator: str) -> int:
        if operator == '+':
            return l+r
        elif operator == '-':
            return l - r
        elif operator == '*':
            return l * r
        elif operator == '/':
            return int(l / r)