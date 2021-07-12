# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        (answer, left, right) = (0, 1, n);
        
        while (left <= right):
            mid = (left + right) // 2;
            
            # print(mid);
            
            if (isBadVersion(mid)):
                answer = mid;
                right = mid - 1;
            else:
                left = mid + 1;
                
        return answer;
