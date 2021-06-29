KEYBOARD_LEN = 26;

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        answer = 0;
        curFinger = 0;
        alphabetDict = dict();
        
        for curIdx in range(KEYBOARD_LEN):
            alphabetDict[keyboard[curIdx]] = curIdx;
            
        # print(alphabetDict);
        
        for curCh in word:
            answer += abs(alphabetDict[curCh] - curFinger);
            curFinger = alphabetDict[curCh];
            
        return answer;
