# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodeCntA = 0;
        nodeCntB = 0;
        curNodeA = headA;
        curNodeB = headB;
        
        # print(curNodeA);
        # print(curNodeB);
        
        while (curNodeA is not None):
            nodeCntA += 1;
            curNodeA = curNodeA.next;
        
        while (curNodeB is not None):
            nodeCntB += 1;
            curNodeB = curNodeB.next;
            
        # print(nodeCntA, nodeCntB);    
        
        curNodeA = headA;
        curNodeB = headB;
        
        while (nodeCntA > nodeCntB):
            curNodeA = curNodeA.next;
            nodeCntA -= 1;
            
        while (nodeCntA < nodeCntB):
            curNodeB = curNodeB.next;
            nodeCntB -= 1;
            
        while (curNodeA is not None):
            if (curNodeA == curNodeB):
                return curNodeA;
            
            curNodeA = curNodeA.next;
            curNodeB = curNodeB.next;
        
        return None;
