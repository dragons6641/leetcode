import collections;

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0;
        numCounter = collections.Counter(nums);
        
        # print(numCounter);
        
        for curKey in numCounter:
            if (numCounter[curKey] == 1):
                answer = curKey;
                
                break;
        
        return answer;
