# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        (curNode, srcNode, dstNode) = (head, head, head);
        (keepCnt, removeCnt) = (0, 0);
        
        while (curNode):
            if (keepCnt < m):
                srcNode = curNode;
                keepCnt += 1;
            else:
                if (removeCnt < n):
                    dstNode = curNode;
                    removeCnt += 1;
                else:
                    # print(curNode.val, srcNode.val, dstNode.val);
                    
                    srcNode.next = dstNode.next;
                    srcNode = dstNode.next;
                    (keepCnt, removeCnt) = (1, 0);
            
            # print(curNode.val, keepCnt, removeCnt);
            
            curNode = curNode.next;
            
        srcNode.next = None;
            
        return head;
