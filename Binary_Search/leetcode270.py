# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

MAX_VAL = 10 ** 9;
MIN_TARGET = -(10 ** 9);
MAX_TARGET = 10 ** 9;

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        answer = root.val;
        minDiff = MAX_VAL - MIN_TARGET;
        curNode = root;
        
        while (curNode):
            if (curNode.val == target):
                return curNode.val;
            
            curDiff = abs(curNode.val - target);
            
            if (minDiff > curDiff):
                answer = curNode.val;
                minDiff = curDiff;
            
            if (curNode.val > target):
                curNode = curNode.left;
            else:
                curNode = curNode.right;
        
        return answer;
