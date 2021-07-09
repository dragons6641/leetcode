# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def checkSame(curNode : TreeNode, curSubNode : TreeNode) -> bool:
    # print('curNode(checkSame) =', curNode.val, 'curSubNode(checkSame) =', curSubNode.val);
    
    if ((curNode.left) and (curSubNode.left)):
        if (curNode.left.val != curSubNode.left.val) or (not checkSame(curNode.left, curSubNode.left)):
            # print("CASE 1-1");
            
            return False;
    elif ((curNode.left) or (curSubNode.left)):
        # print("CASE 1-2");
        
        return False;
    
    if ((curNode.right) and (curSubNode.right)):
        if (curNode.right.val != curSubNode.right.val) or (not checkSame(curNode.right, curSubNode.right)):
            # print("CASE 2-1");
            
            return False;
    elif ((curNode.right) or (curSubNode.right)):
        # print("CASE 2-2");
        
        return False;
    
    return True;

def traverseTree(curNode : TreeNode, subRoot : TreeNode) -> bool:       
    if (curNode.val == subRoot.val) and (checkSame(curNode, subRoot)):
        # print(checkSame(curNode, subRoot));
        
        return True;
        
    if ((curNode.left) and (traverseTree(curNode.left, subRoot))):
        return True;
        
    if ((curNode.right) and (traverseTree(curNode.right, subRoot))):
        return True;
        
    # print('curNode(traverseTree) =', curNode.val, 'subRoot(traverseTree) =', subRoot.val);
        
    return False;

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        return (traverseTree(root, subRoot));
