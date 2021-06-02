MAX_LEN = 3 * (10 ** 4);
MAX_NUM = 10 ** 5;
INF = MAX_LEN * MAX_NUM;

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = -INF;
        curSum = 0;
        
        for curNum in nums:
            curSum += curNum;
            
            if (answer < curSum):
                answer = curSum;
            
            if (curSum < 0):
                curSum = 0;
                
        return answer;
