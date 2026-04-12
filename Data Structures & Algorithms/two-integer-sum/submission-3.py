class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       # Two pointer technique
       # Sort the arr
       arr = []
       for i, num in enumerate(nums):
        arr.append([num, i])
       arr.sort()
       n = len(nums)
       left = 0
       right = n - 1
       while left < right:
        sum = arr[left][0] + arr[right][0]
        if sum == target:
            return sorted([arr[left][1],arr[right][1]])
        if sum < target:
            left +=1
        if sum > target:
            right -=1
