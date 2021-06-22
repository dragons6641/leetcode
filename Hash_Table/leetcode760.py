class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = [];
        
        for num1 in nums1:
            answer.append(nums2.index(num1));
            
        return answer;
