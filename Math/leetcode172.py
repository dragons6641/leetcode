import math;

class Solution:
    def trailingZeroes(self, n: int) -> int:
        answer = 0;
        baseNum = 5;
        
        while (baseNum <= n):
            for jumpNum in range(baseNum, n + 1, baseNum):
                answer += 1;
            
            baseNum *= 5;
            
        return answer;
