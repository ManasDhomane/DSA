class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        ans = n

        for i in range(n):
            if words[i] == target:
                distance = abs(i - startIndex)
                distance = min(distance, n - distance)
                ans = min(ans, distance)

        if ans == n:
            return -1

        return ans