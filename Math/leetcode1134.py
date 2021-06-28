class Solution:
    def isArmstrong(self, n: int) -> bool:
        strNum = str(n);
        numLen = len(strNum);
        digitPowerSum = 0;
        
        for curCh in strNum:
            digitPowerSum += int(curCh) ** numLen;
            
        return (digitPowerSum == n);
