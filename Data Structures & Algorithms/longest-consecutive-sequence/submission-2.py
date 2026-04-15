class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums2 = sorted(set((nums)))
        output = 1
        prev = nums2[0]
        for i in range(1, len(nums2)):
            num = nums2[i]
            if num != prev + 1:
                return output
            prev = num
            output += 1
        return output