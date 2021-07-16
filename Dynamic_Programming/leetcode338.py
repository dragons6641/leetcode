class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(k).count('1') for k in range(n + 1)];
