class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 1];
        
        for k in range(2, n + 1):
            dp.append(dp[k - 1] + dp[k - 2]);
            
        return dp[n];
