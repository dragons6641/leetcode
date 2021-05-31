romanNumeralValueDict = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000};
romanNumeralSymbolDict = {'I' : ('V', 'X'), 'X' : ('L', 'C'), 'C' : ('D', 'M')};

class Solution:
    def romanToInt(self, s: str) -> int:
        # print(romanNumeralValueDict);
        # print(romanNumeralSymbolDict);
        
        answer = 0;
        curIdx = 0;
        sLen = len(s);
        
        while (curIdx < sLen):
            curSymbol = s[curIdx];
            curValue = romanNumeralValueDict[curSymbol];
            
            if (curIdx == sLen - 1):
                answer += curValue;
                
                break;
                
            nextSymbol = s[curIdx + 1]; 
            nextValue = romanNumeralValueDict[nextSymbol];
            
            if ((curSymbol in romanNumeralSymbolDict.keys()) and (nextSymbol in romanNumeralSymbolDict[curSymbol])):
                answer += nextValue - curValue;
                curIdx += 2;
            else:
                answer += curValue;
                curIdx += 1;
                
        return answer;
