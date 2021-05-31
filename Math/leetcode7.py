import collections;

DIGIT = 10;
MIN_INF = -(2**31);
MAX_INF = -(MIN_INF + 1);

class Solution:
    def reverse(self, x: int) -> int:
        answer = 0;
        dq = collections.deque(list(str(x)));
        dq.reverse();
        
        if (x < 0):
            dq.appendleft(dq.pop());
            
        for curCh in dq:
            if (curCh != '-'):
                answer = (answer * 10) + int(curCh);
        
        if (x < 0):
            answer = (-answer);
            
        if ((answer < MIN_INF) or (answer > MAX_INF)):
            answer = 0;
        
        return answer;
