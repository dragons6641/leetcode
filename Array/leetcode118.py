class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [];
        
        for r in range(numRows):
            tmpList = [];
            
            for c in range(r + 1):
                # print(r, c);
                
                if ((c == 0) or (c == r)):
                    tmpList.append(1);
                else:
                    tmpList.append(answer[r - 1][c - 1] + answer[r - 1][c]);
                    
            answer.append(tmpList);
                    
        return answer;
