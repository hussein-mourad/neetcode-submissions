class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        target = 0
        # [-4, -1, -1, 0, 1, 2]
        res = []
        for i in range(n - 2):
            l = i + 1
            r = n - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    pair = [nums[i], nums[l], nums[r]]
                    if pair not in res:
                        res.append(pair)
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    r -=1
        return res