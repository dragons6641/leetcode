class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        answer = [];
        (letterLogList, digitLogList) = ([], []);
        
        for curLog in logs:
            splitLog = curLog.split();
            
            if (not splitLog[1].isdigit()):
                letterLogList.append([splitLog[0], ' '.join(splitLog[1 : ])]);
            else:
                digitLogList.append(curLog);
                
        # print(letterLogList);
        # print(digitLogList);
        
        letterLogList.sort(key = lambda k : (k[1], k[0]));
        
        for curLetterLog in letterLogList:
            answer.append(' '.join(curLetterLog));
        
        answer.extend(digitLogList);
        
        # print(answer);
        
        return answer;
