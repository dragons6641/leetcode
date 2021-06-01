class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:       
        leftIdx = 0;
        rightIdx = 1;
        
        while (rightIdx < len(nums)):
            leftVal = nums[leftIdx];
            rightVal = nums[rightIdx];
            
            if (leftVal == rightVal):
                rightIdx += 1;
                
                continue;
                
            if (rightIdx - leftIdx > 1):
                del nums[leftIdx + 1 : rightIdx];
                
            leftIdx += 1;
            rightIdx = leftIdx + 1;
        
        if (rightIdx - leftIdx > 1):
            del nums[leftIdx + 1 : rightIdx];
        
        answer = len(nums);
        
        return answer;
