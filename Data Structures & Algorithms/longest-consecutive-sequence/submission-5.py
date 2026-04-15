class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums2 = sorted(set((nums)))
        longest = 1
        curr = 1
        prev = nums2[0]
        for i in range(1, len(nums2)):
            num = nums2[i]
            if num != prev + 1:
                curr = 1
                prev = num
                continue
            prev = num
            curr += 1
            longest = max(longest, curr)
        return longest