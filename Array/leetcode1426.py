import collections;

class Solution:
    def countElements(self, arr: List[int]) -> int:
        answer = 0;
        arrCounter = collections.Counter(arr);
        
        for (curKey, curVal) in arrCounter.items():
            if (curKey + 1) in arrCounter.keys():
                answer += curVal;
                
        return answer;
