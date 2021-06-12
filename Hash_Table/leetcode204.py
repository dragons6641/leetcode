import math;

class Solution:
    def countPrimes(self, n: int) -> int:
        if (n <= 1):
            return 0;
        
        answer = n - 2;
        sqrtN = math.ceil(math.sqrt(n));
        
        isPrimeList = [True for _ in range(n)];
        isPrimeList[0] = False;
        isPrimeList[1] = False;
        
        for i in range(2, sqrtN):
            if (not isPrimeList[i]):
                continue;
            
            for j in range(i * 2, n, i):
                if (isPrimeList[j]):
                    answer -= 1;
                    isPrimeList[j] = False;
                
        # print(isPrimeList);
        
        return answer;
