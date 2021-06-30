class Solution:
    def countLetters(self, s: str) -> int:
        answer = 0;
        distinctCnt = 0;
        distinctCh = '';
        
        for curCh in s:
            if (curCh == distinctCh):
                distinctCnt += 1;
            else:
                answer += ((distinctCnt / 2) * (distinctCnt + 1));
                distinctCnt = 1;
                distinctCh = curCh;
                
        answer += ((distinctCnt / 2) * (distinctCnt + 1));
        
        return int(answer);
