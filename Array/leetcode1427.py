import collections;

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        dq = collections.deque(s);
        
        for (curDirection, curAmount) in shift:
            dq.rotate(-curAmount if (curDirection == 0) else curAmount);
        
        return "".join(dq);
