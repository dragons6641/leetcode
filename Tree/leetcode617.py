# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def sumTree(src1 : TreeNode, src2 : TreeNode) -> TreeNode:
    if ((not src1) and (not src2)):
        return None;
    
    dst = TreeNode();
    
    if ((src1) and (src2)):
        dst.val = src1.val + src2.val;
        dst.left = sumTree(src1.left, src2.left);
        dst.right = sumTree(src1.right, src2.right);
    elif (src1):
        dst.val = src1.val;
        dst.left = sumTree(src1.left, None);
        dst.right = sumTree(src1.right, None);
    elif (src2):
        dst.val = src2.val;
        dst.left = sumTree(None, src2.left);
        dst.right = sumTree(None, src2.right);
    
    return dst;

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        return sumTree(root1, root2);
