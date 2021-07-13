class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        (target, left, right) = (-1, 0, len(arr) - 1);
        
        while (left <= right):
            mid = (left + right) // 2;
            
            if (arr[mid] - mid - 1 < k):
                target = mid;
                left = mid + 1;
            else:
                right = mid - 1;
                
        # print(target);
        
        return (k + target + 1);
