class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        res=0
        prefix = [0] * n
        for  i in range(1, n - 1):
           prefix[i] = max(height[i-1], prefix[i - 1])
        suffix = [0] * n
        for i in range(n - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], height[i + 1])
        for i, w in enumerate(height):
            curr = min(prefix[i], suffix[i]) - w
            if curr > 0:
                res+=curr
        return res