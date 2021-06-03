# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

leftOrderList = [];
rightOrderList = [];

def preOrder(root, mode):
    if (mode == 1):
        leftOrderList.append(root.val);
        
        if (root.left is None):
            leftOrderList.append(None);
        else:
            preOrder(root.left, mode);
        
        if (root.right is None):
            leftOrderList.append(None);
        else:
            preOrder(root.right, mode);
        
    elif (mode == 2):
        rightOrderList.append(root.val);
        
        if (root.right is None):
            rightOrderList.append(None);
        else:
            preOrder(root.right, mode);
        
        if (root.left is None):
            rightOrderList.append(None);
        else:
            preOrder(root.left, mode);
    
    return;

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # print(root);
        # print(root.left);
        # print(root.right);
        
        global leftOrderList;
        global rightOrderList;
        
        leftOrderList = [];
        rightOrderList = [];
        
        if (root.left is not None):
            preOrder(root.left, 1);
        
        if (root.right is not None):
            preOrder(root.right, 2);
        
        # print(leftOrderList);
        # print(rightOrderList);
        # print();
        
        return (leftOrderList == rightOrderList);
