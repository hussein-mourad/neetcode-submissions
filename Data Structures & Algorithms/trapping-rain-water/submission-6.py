class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        for i in range(n):
            curr = height[i]
            max_l = curr
            for j in range(i, 0, -1):
                max_l = max(max_l, height[j])
            max_r = curr
            for j in range(i, n):
                max_r = max(max_r, height[j])
            current_height = min(max_l, max_r) - curr
            res += current_height
        return res
