class Solution:
    def numWaterBottles(self, n: int, a: int) -> int:
        return int(n + ((n - 1)/(a-1)))

        