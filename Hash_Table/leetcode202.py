DIGIT = 10;

class Solution:
    def isHappy(self, n: int) -> bool:
        curNum = n;
        numSet = set();
        
        while (True):
            curSquareSum = 0;
            
            while (curNum > 0):
                curSquareSum += (curNum % DIGIT) ** 2;
                curNum //= DIGIT;
            
            if (curSquareSum == 1):
                return True;
            elif (curSquareSum in numSet):
                return False;
            
            curNum = curSquareSum;
            numSet.add(curSquareSum);
            
        return None;
