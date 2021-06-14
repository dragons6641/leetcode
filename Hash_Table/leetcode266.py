import collections;

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        oddCnt = 0;
        sCounter = collections.Counter(s);
        
        # print(sCounter);
        
        for (curKey, curVal) in sCounter.items():
            # print(curKey, curVal);
            
            if (curVal % 2 == 0):
                continue;
        
            if (oddCnt == 1):
                return False;
        
            oddCnt += 1;
            
        return True;
