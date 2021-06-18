# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

answer = 0;

def findMaxLevel(curNode : TreeNode, curLevel : int) -> int:
    if (not curNode):
        return (curLevel - 1);
    
    global answer;
    
    leftMaxLevel = findMaxLevel(curNode.left, curLevel + 1);
    rightMaxLevel = findMaxLevel(curNode.right, curLevel + 1);
    curDiameter = leftMaxLevel + rightMaxLevel - (curLevel * 2);
    answer = max(answer, curDiameter);
    
    # print(curNode.val);
    # print(leftMaxLevel, rightMaxLevel, curDiameter, answer);
    
    return max(leftMaxLevel, rightMaxLevel);
    
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        global answer;
        
        answer = 0;
        
        findMaxLevel(root, 0);
        
        return answer;
