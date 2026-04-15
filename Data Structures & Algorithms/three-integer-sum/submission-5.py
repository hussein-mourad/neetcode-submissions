class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        target = 0
        res = []
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            curr = nums[i]
            # Break early if the curr is +ve 
            # Since it is a sorted array all other element to the left 
            # will be +ve so it will increase the sum
            if curr > target:
                break
            # Skip duplicates
            if i > 0 and curr == nums[i-1]:
                continue

            while l < r:
                s = curr + nums[l] + nums[r]
                if s == target:
                    pair = [curr, nums[l], nums[r]]
                    # Skip duplicates
                    # if pair not in res:
                    res.append(pair)
                    l += 1
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    r -=1
        return res