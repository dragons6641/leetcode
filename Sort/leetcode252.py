MAX_TIME = 10 ** 6;

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sortedIntervals = sorted(intervals, key = lambda k : (k[0], -k[1]));
        
        # print(sortedIntervals);
        
        for curIdx in range(len(sortedIntervals) - 1):
            if (sortedIntervals[curIdx][1] > sortedIntervals[curIdx + 1][0]):
                return False;
            
        return True;
