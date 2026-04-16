class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        for i in range(1, n - 1):
            curr = height[i]
            l, r = i - 1, i + 1
            max_l, max_r = height[l], height[r]
            while l > 0:
                max_l = max(max_l, height[l])
                l -= 1
            while r < n - 1:
                max_r = max(max_r, height[r])
                r += 1
            if max_l < curr or max_r < curr:
                continue
            current_height = min(max_l, max_r) - curr
            res += current_height
        return res
