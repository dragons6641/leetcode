class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        numRows = len(words);
        numColumns = max(len(words[r]) for r in range(numRows));
        n = max(numRows, numColumns);
        
        wordArray = [['' for c in range(n)] for r in range(n)];
        
        # print(numRows, numColumns);
        
        for r in range(numRows):
            for c in range(len(words[r])):
                wordArray[r][c] = words[r][c];
                
        for r in range(n):
            for c in range(0, r):
                # print(r, c);
                
                if (wordArray[r][c] != wordArray[c][r]):
                    return False;
                
        # print(wordArray);
        
        return True;
