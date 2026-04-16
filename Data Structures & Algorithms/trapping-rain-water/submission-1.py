class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        for i in range(1, n - 1):
            curr = height[i]
            l, r = i - 1, i + 1
            while l > 0 and curr > height[l]:
                l -= 1
            while r < n - 1 and curr > height[r]:
                r += 1
            current_height = min(height[l], height[r]) - curr
            res += current_height
        return res
