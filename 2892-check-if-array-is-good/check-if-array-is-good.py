class Solution:
    def isGood(self, nums):
        n = max(nums)
        if len(nums) != n + 1:
            return False
        nums.sort()
        for i in range(n - 1):
            if nums[i] != i + 1:
                return False
        return nums[-1] == n and nums[-2] == n