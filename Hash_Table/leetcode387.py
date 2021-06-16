import collections;

MAX_LEN = 10 ** 5;

class Solution:
    def firstUniqChar(self, s: str) -> int:
        answer = MAX_LEN;
        sCounter = collections.Counter(s);
        
        # print(sCounter);
        
        for (curKey, curVal) in sCounter.items():
            if (curVal == 1):
                answer = min(answer, s.index(curKey));
                
        if (answer == MAX_LEN):
            answer = -1;
            
        return answer;
