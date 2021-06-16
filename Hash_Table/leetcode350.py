import collections;

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = [];
        intersectCounter = collections.Counter(nums1) & collections.Counter(nums2);
        
        # print(intersectCounter);
        
        for (curKey, curVal) in intersectCounter.items():
            answer.extend([curKey for _ in range(curVal)]);
            
        return answer;
