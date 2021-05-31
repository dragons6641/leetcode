class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if (len(strs) == 1):
            return strs[0];
        
        answer = "";
        curIdx = 0;
        
        strs.sort();
        
        # print(strs);
        
        minLen = min(len(strs[0]), len(strs[-1]));
        
        while (curIdx < minLen):
            firstCh = strs[0][curIdx];
            lastCh = strs[-1][curIdx];
            
            if (firstCh == lastCh):
                answer += firstCh;
            else:
                break;
                
            curIdx += 1;
            
        return answer;
