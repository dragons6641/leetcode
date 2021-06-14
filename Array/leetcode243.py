MAX_LEN = 3 * (10 ** 4);

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        answer = MAX_LEN;
        idx1 = 0;
        idx2 = 0;
        word1IdxList = [];
        word2IdxList = [];
        
        for curIdx in range(len(wordsDict)):
            curWord = wordsDict[curIdx];
            
            if (curWord == word1):
                word1IdxList.append(curIdx);
            elif (curWord == word2):
                word2IdxList.append(curIdx);
        
        # print(word1IdxList);
        # print(word2IdxList);
        
        while ((idx1 < len(word1IdxList)) and (idx2 < len(word2IdxList))):
            word1Idx = word1IdxList[idx1];
            word2Idx = word2IdxList[idx2];
            
            answer = min(answer, abs(word1Idx - word2Idx));
            
            if (word1Idx < word2Idx):
                idx1 += 1;
            else:
                idx2 += 1;
                
        return answer;
