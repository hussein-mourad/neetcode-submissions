class MinStack:

    def __init__(self):
        self._stack = []
        

    def push(self, val: int) -> None:
        self._stack.append(val)

    def pop(self) -> None:
        self._stack.pop()
        

    def top(self) -> int:
        return self._stack[-1]
        

    def getMin(self) -> int:
        min_item = self._stack[0]
        for item in self._stack:
            min_item = min(min_item, item)
        return min_item
        
