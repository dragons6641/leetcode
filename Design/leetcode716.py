class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [];
        
        return None;

    def push(self, x: int) -> None:
        self.stack.append(x);
        
        return None;

    def pop(self) -> int:
        return self.stack.pop();

    def top(self) -> int:
        return self.stack[-1];

    def peekMax(self) -> int:
        return max(self.stack);

    def popMax(self) -> int:
        return self.stack.pop(len(self.stack) - list(reversed(self.stack)).index(max(self.stack)) - 1);

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
