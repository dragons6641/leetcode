class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedNums = sorted(nums);
        numLen = len(sortedNums);
        leftIdx = 0;
        rightIdx = numLen - 1;
        
        while (leftIdx < rightIdx):
            leftVal = sortedNums[leftIdx];
            rightVal = sortedNums[rightIdx];
            twoSum = leftVal + rightVal;
            
            # print(twoSum);
            # print(leftIdx, rightIdx);
            # print(sortedNums[leftIdx], sortedNums[rightIdx]);
            # print();
            
            if (twoSum < target):
                leftIdx += 1;
            elif (twoSum > target):
                rightIdx -= 1;
            else:
                leftAnswer = nums.index(leftVal);
                rightAnswer = nums.index(rightVal);
                
                if (leftAnswer == rightAnswer):
                    rightAnswer = nums.index(rightVal, leftAnswer + 1, numLen);
                
                return [leftAnswer, rightAnswer];
            
        return [-1, numLen];
