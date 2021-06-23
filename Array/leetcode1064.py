class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        answer = -1;
        left = 0;
        right = len(arr) - 1;
        
        while (left <= right):
            mid = (left + right) // 2;
            diff = mid - arr[mid];
            
            # print(left, right, mid, arr[mid], diff);
                    
            if (diff < 0):
                right = mid - 1;
            elif (diff > 0):
                left = mid + 1;
            else:
                right = mid - 1;
                answer = mid;
            
        return answer;
