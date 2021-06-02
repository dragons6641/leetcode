MAX_LEN = 100;
MAX_DIGIT = 10;

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0;
        answer = [];
        
        for curDigit in digits:
            num = (num * MAX_DIGIT) + curDigit;
            
            # print(num, curDigit);
            
        num += 1;
        
        # print(num);
        
        while (num > 0):
            answer.append(num % MAX_DIGIT);
            num //= MAX_DIGIT;
            
        answer.reverse();
                
        return answer;
