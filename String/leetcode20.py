bracketDict = {')' : '(', '}' : '{', ']' : '['};

class Solution:
    def isValid(self, s: str) -> bool:
        stack = [];
        
        for curCh in s:
            if (curCh in bracketDict.values()):
                stack.append(curCh);
                
                continue;
                
            if ((len(stack) == 0) or (bracketDict[curCh] != stack[-1])):
                return False;
            
            stack.pop();
            
        if (len(stack) > 0):
            return False;
            
        return True;
