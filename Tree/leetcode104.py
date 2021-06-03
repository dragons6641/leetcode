# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

answer = 0;

def preOrder(subTree, depth):
    global answer;
    
    answer = max(answer, depth);
    
    if (subTree.left is not None):
        preOrder(subTree.left, depth + 1);
        
    if (subTree.right is not None):
        preOrder(subTree.right, depth + 1);
        
    return;

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # print(root);
        
        global answer;
        
        answer = 0;
        
        if (root is not None):
            preOrder(root, 1);
        
        return answer;
