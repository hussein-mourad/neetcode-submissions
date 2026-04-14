class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        prod = 1
        for num in nums:
            prod *= num
        
        for i, num in enumerate(nums):
            if num != 0:
                output[i] = int(prod / num)
        return output