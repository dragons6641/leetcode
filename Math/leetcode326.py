import math;

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        powerOfThree = 1;
        
        while (powerOfThree <= n):
            if powerOfThree == n:
                return True;
            
            powerOfThree *= 3;
            
        return False;
