class Solution:
    def minimumDistance(self, nums):
        n = len(nums)
        ans = float('inf')

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):

                    if nums[i] == nums[j] == nums[k]:
                        distance = 2 * (k - i)
                        ans = min(ans, distance)

        if ans == float('inf'):
            return -1

        return ans