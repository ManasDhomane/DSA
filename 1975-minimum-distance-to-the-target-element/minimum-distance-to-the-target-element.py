class Solution:
    def getMinDistance(self, nums, target, start):
        min_distance = float('inf')

        for i in range(len(nums)):
            if nums[i] == target:
                distance = abs(i - start)
                min_distance = min(min_distance, distance)

        return min_distance