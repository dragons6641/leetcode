import collections;

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        (majorityElement, majorityCnt) = collections.Counter(nums).most_common(1)[0];
        
        # print(majorityElement, majorityCnt);
        
        return ((majorityElement == target) and (majorityCnt > len(nums) // 2));
