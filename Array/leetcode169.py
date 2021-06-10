import collections;

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numCounter = collections.Counter(nums);
        
        # print(numCounter);
        
        answer = numCounter.most_common()[0][0];
        
        # print(answer);
        
        return answer;
