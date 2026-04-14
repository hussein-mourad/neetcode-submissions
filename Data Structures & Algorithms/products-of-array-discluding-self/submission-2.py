class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        output = []
        for i in range(n):
            prod = 1
            for j in range(n):
                if j == i:
                    continue
                prod *= nums[j]
            prefix[i] = prod
        for i in range(n, -1, -1):
            prod = 1
            for j in range(n, -1, -1):
                if j == i:
                    continue
                prod *= nums[j]
            suffix[j] = prod
        for p, s in zip(prefix, suffix):
            output.append(p*s)
