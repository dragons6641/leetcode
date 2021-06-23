class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        answer = [];
        
        for curWord in words:
            curIdx = 0;
            curLen = len(curWord);
            
            while (True):
                findIdx = text.find(curWord, curIdx);
                
                if (findIdx == -1):
                    break;
                    
                answer.append([findIdx, findIdx + curLen - 1]);
                curIdx = findIdx + 1;
        
        answer.sort();
        
        # print(answer);
        
        return answer;
