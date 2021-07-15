def getNextReplaceCh(curReplaceCh : str) -> str:
    return ('a' if (curReplaceCh == 'z') else chr(ord(curReplaceCh) + 1));

class Solution:
    def modifyString(self, s: str) -> str:
        (answer, replaceCh) = ('', 'a');
        
        if (len(s) == 1):
            return (replaceCh if (s == '?') else s);
        
        if (s[0] == '?'):
            while (s[1] == replaceCh):
                replaceCh = getNextReplaceCh(replaceCh);
            
            answer += replaceCh;
        else:
            answer += s[0];
            
        for chIdx in range(1, len(s) - 1):
            if (s[chIdx] == '?'):
                while ((answer[-1] == replaceCh) or (s[chIdx + 1] == replaceCh)):
                    replaceCh = getNextReplaceCh(replaceCh);
                    
                    # print(replaceCh);
                    # print(answer);
                    
                answer += replaceCh;
            else:
                answer += s[chIdx];
            
        if (s[-1] == '?'):
            while (answer[-1] == replaceCh):
                replaceCh = getNextReplaceCh(replaceCh);
            
            answer += replaceCh;
        else:
            answer += s[-1];
            
        return answer;
