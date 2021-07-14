STROBOGRAMMATIC_LIST = [0, 0, -1, -1, -1, -1, 9, -1, 0, 6];

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        (leftIdx, rightIdx) = (0, len(num) - 1);
        
        while (leftIdx < rightIdx):
            (leftDigit, rightDigit) = (int(num[leftIdx]), int(num[rightIdx]));
            
            if ((STROBOGRAMMATIC_LIST[leftDigit] == -1) or (STROBOGRAMMATIC_LIST[rightDigit] == -1)):
                return False;
            
            strobogrammaticSum = STROBOGRAMMATIC_LIST[leftDigit] + STROBOGRAMMATIC_LIST[rightDigit];
            
            if (strobogrammaticSum == 0):
                if (leftDigit != rightDigit):
                    return False;
            elif (strobogrammaticSum != 15):
                return False;
            
            (leftIdx, rightIdx) = (leftIdx + 1, rightIdx - 1);
            
        if ((leftIdx == rightIdx) and (STROBOGRAMMATIC_LIST[int(num[leftIdx])] != 0)):
            return False;
            
        return True;
