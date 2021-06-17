class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [str(i) for i in range(1, n + 1)];
        
        for curIdx in range(2, n, 3):
            answer[curIdx] = "Fizz";
            
        for curIdx in range(4, n, 5):
            answer[curIdx] = "Buzz";
                
        for curIdx in range(14, n, 15):
            answer[curIdx] = "FizzBuzz";
        
        # print(answer);
        
        return answer;
