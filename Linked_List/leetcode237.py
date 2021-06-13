# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        curNode = node;
        
        while (True):
            curNode.val = curNode.next.val;
            
            if (curNode.next.next):
                curNode = curNode.next;
            else:
                break;
        
        # print(curNode);
        
        curNode.next = None;
        
        return None;
