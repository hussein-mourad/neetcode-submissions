class Solution:
    def binary_search(self, l: int, r: int, nums: List[int], target: int):
        if l > r:
            return -1
        m = l + (r - l) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        return self.binary_search(l, r, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)