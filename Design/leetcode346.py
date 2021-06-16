class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size;
        self.lp = 0;
        self.rp = -1;
        self.valSum = 0;
        self.valList = [];
        
        return None;

    def next(self, val: int) -> float:
        # print(self.size, self.lp, self.rp, self.valSum);
        # print(self.valList);
        
        self.rp += 1;
        self.valSum += val;
        self.valList.append(val);
        
        if (self.rp - self.lp >= self.size):
            self.valSum -= self.valList[self.lp];
            self.lp += 1;
            
        return (self.valSum / (self.rp - self.lp + 1));

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
