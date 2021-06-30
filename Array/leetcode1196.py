MAX_WEIGHT = 5000;

class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        answer = len(arr);
        curSum = sum(arr);
        
        if (curSum <= MAX_WEIGHT):
            return answer;
        
        arr.sort(reverse = True);
        
        # print(arr);
        
        for curWeight in arr:
            answer -= 1;
            curSum -= curWeight;
            
            if (curSum <= MAX_WEIGHT):
                break;
            
        return answer;
