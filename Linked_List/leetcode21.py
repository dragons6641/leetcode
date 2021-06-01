# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # print(l1, l2);
        
        answer = ListNode();
        p0 = answer;
        p1 = l1;
        p2 = l2;

        while ((p1 != None) and (p2 != None)):
            p0.next = ListNode();
            p0 = p0.next;
            
            val1 = p1.val;
            val2 = p2.val;
            
            if (val1 < val2):
                p0.val = val1;
                p1 = p1.next;
            else:
                p0.val = val2;
                p2 = p2.next;
            
        # print(answer);
        
        while (p1 != None):
            p0.next = ListNode();
            p0 = p0.next;
            p0.val = p1.val;
            p1 = p1.next;
            
        while (p2 != None):
            p0.next = ListNode();
            p0 = p0.next;
            p0.val = p2.val;
            p2 = p2.next;
            
        answer = answer.next;
        
        return answer;
