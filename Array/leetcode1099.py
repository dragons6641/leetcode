class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        answer = -1;
        leftIdx = 0;
        rightIdx = len(nums) - 1;
        
        nums.sort();
        
        # print(nums);
        
        while (leftIdx < rightIdx):
            twoSum = nums[leftIdx] + nums[rightIdx];
            
            if (twoSum < k):
                answer = max(answer, twoSum);
                leftIdx += 1;
            else:
                rightIdx -= 1;
                    
        return answer;
