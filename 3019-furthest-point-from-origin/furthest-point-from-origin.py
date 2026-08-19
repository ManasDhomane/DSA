class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        L = moves.count('L')
        R = moves.count('R')
        blank = moves.count('_')

        right = R + blank - L
        left = L + blank - R

        return max(abs(right), abs(left))