DIGIT = 26;
BIAS = ord('A') - 1;

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        answer = 0;
        
        for curCh in columnTitle:
            answer = (answer * DIGIT) + ord(curCh) - BIAS;
            
        return answer;
