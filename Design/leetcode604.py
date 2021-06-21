DIGIT = 10;

class StringIterator:
    def __init__(self, compressedString: str):
        self.chCnt = 0;
        self.strIdx = 0;
        self.orgCh = "";
        self.orgStr = "";
        
        for curCh in compressedString:
            if curCh.isdigit():
                self.chCnt = (self.chCnt * DIGIT) + int(curCh);
            else:
                self.orgStr += (self.orgCh * self.chCnt);
                self.chCnt = 0;
                self.orgCh = curCh;
          
        self.orgStr += (self.orgCh * self.chCnt);
        
        # print(self.orgStr);

    def next(self) -> str:
        if (self.hasNext()):
            self.strIdx += 1;
            
            return (self.orgStr[self.strIdx - 1]);
        
        return " ";

    def hasNext(self) -> bool:
        return (self.strIdx < len(self.orgStr));

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
