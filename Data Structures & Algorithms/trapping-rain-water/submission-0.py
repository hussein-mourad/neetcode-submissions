class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        for i in range(n - 1):
            l, r = i - 1, i + 1
            curr = height[i]
            # Get left bound
            while l < 0 and curr > height[l]:
                l -= 1
            while r < n - 1 and curr > height[r]:
                r += 1
            # if l < 0:
            #     l = i
            # if r == n:
            #     r = i
            t = min(height[l], height[r]) - curr
            res += t
        return t

