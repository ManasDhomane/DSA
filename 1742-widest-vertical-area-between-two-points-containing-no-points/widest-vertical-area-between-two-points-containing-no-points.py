class Solution:
    def maxWidthOfVerticalArea(self, points):
        x = []

        for point in points:
            x.append(point[0])

        x.sort()

        ans = 0

        for i in range(1, len(x)):
            ans = max(ans, x[i] - x[i - 1])

        return ans