class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = str(bin(n))[2:].count('1');
        
        return answer;
