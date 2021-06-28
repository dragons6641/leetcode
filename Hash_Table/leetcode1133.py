import collections;

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        numCounter = collections.Counter(nums);
        sortedList = sorted(list(zip(numCounter.keys(), numCounter.values())), key = lambda k : (k[1], -k[0]));
        
        return sortedList[0][0] if (sortedList[0][1] == 1) else -1;
