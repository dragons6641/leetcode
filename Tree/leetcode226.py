# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def preOrder(curNode : TreeNode) -> None:
    if (curNode is None):
        return;
    
    curNode.left, curNode.right = curNode.right, curNode.left;
    
    preOrder(curNode.left);
    preOrder(curNode.right);
 
    return;

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        preOrder(root);
        
        return root;
