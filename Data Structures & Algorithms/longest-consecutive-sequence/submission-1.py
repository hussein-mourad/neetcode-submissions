class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums2 = list(set(sorted(nums)))
        output = 1
        prev = nums2[0]
        for i in range(1, len(nums2)):
            num = nums2[i]
            if num - 1 != prev:
                return output
            prev = num
            output += 1
        return output