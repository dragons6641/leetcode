class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        answer = [];
        
        nums.append(lower - 1);
        nums.append(upper + 1);
        nums.sort();
        
        for curIdx in range(len(nums) - 1):
            rangeStart = nums[curIdx] + 1;
            rangeEnd = nums[curIdx + 1] - 1;
            
            if (rangeStart == rangeEnd):
                answer.append(str(rangeStart));
            elif (rangeStart < rangeEnd):
                answer.append(str(rangeStart) + '->' + str(rangeEnd));
            
        # print(answer);

        return answer;
