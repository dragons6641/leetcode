class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.numDict = {};
        
        return;

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        
        if (number in self.numDict.keys()):
            self.numDict[number] += 1;
        else:
            self.numDict[number] = 1;
        
        return;

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        
        for firstNum in self.numDict.keys():
            secondNum = value - firstNum;
            
            if (secondNum not in self.numDict.keys()):
                continue;
            
            if (firstNum == secondNum):
                if (self.numDict[secondNum] >= 2):
                    return True;
            else:
                if (self.numDict[secondNum] >= 1):
                    return True;
                
        return False;
                

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
