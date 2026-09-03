class Solution:
    def minimumOperations(self, nums):
        return len(set(num for num in nums if num > 0))