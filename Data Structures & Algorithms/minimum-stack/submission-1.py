class MinStack:

    def __init__(self):
        self._len = 0
        self._stack = []
        

    def push(self, val: int) -> None:
        self._len += 1
        self._stack = self._stack + [val]

    def pop(self) -> None:
        if self._len == 0:
            return
        self._len -= 1
        self._stack = self._stack[0:-1]
        

    def top(self) -> int:
        return self._stack[self._len - 1]
        

    def getMin(self) -> int:
        min_item = self._stack[0]
        for item in self._stack:
            min_item = min(min_item, item)
        return min_item
        
