import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.k = k
        for num in nums:
            heapq.heappush(self.h, num)
        print(self.h)

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        return self.h[-self.k]
        
