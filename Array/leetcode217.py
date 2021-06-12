import collections;

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numCounter = collections.Counter(nums);
        
        return (numCounter.most_common(1)[0][1] > 1);
