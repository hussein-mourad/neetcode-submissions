class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        # [1, 2, 3, 4, 5, 6, 7, 7]
        l, r = 0, n - 1
        while l < r:
            a, b = heights[l], heights[r]
            w = r - l
            h = min(a,b)
            area = w * h
            max_area = max(max_area, area)
            if a < b:
                l += 1
            elif b < a:
                r -= 1
            else:
                r -= 1
        return max_area

        