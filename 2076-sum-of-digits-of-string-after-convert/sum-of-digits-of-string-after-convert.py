class Solution:
    def getLucky(self, s: str, k: int) -> int:
        total = 0
        for ch in s:
            value = ord(ch) - ord('a') + 1
            total += value // 10 + value % 10

        for _ in range(k - 1):
            total = sum(int(digit) for digit in str(total))

        return total