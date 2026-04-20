class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res=0
        for i,  w in enumerate(height):
            l, r, curr = 0, 0, 0
            for j in range(i, -1, -1):
                l = max(l, height[j])
            for j in range(i, n):
                r = max(r, height[j])
            curr = min(l, r) - w
            if curr > 0:
                res +=curr
        return res