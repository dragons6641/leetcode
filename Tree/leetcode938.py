# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def traverseTree(curNode : TreeNode, low : int, high : int) -> int:
    answer = 0;
    
    if ((curNode.val >= low) and (curNode.val <= high)):
        answer += curNode.val;
    
    if ((curNode.left) and (curNode.val >= low)):
        answer += traverseTree(curNode.left, low, high);
        
    if ((curNode.right) and (curNode.val <= high)):
        answer += traverseTree(curNode.right, low, high);
    
    return answer;

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        return traverseTree(root, low, high);
