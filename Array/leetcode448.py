import collections;

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numCounter = collections.Counter([i for i in range(1, len(nums) + 1)]) - collections.Counter(nums);
        answer = [curKey for curKey in numCounter.keys()];
        
        # print(numCounter);
        
        return answer;
