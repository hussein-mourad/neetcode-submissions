class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lookup = {}
        for i in nums:
            if i in lookup:
                return True
            lookup[i] = 1
        return False