# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # print(head);
        # print(head.val);
        # print(head.next);
        
        answer = False;
        curNode = head;
        nodeSet = set();
        
        while (curNode is not None):
            if (curNode in nodeSet):
                answer = True;
                
                break;
                
            nodeSet.add(curNode);
            curNode = curNode.next;
        
        return answer;
