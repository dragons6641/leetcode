# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorder(curNode : TreeNode) -> list:
    curResultList = [];
    
    if (not curNode):
        return [];
    
    leftResultList = inorder(curNode.left);
    
    if (leftResultList):
        curResultList.extend(leftResultList);
        
    curResultList.append(curNode.val);
    
    rightResultList = inorder(curNode.right);
    
    if (rightResultList):
        curResultList.extend(rightResultList);
        
    return curResultList;

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return inorder(root);
