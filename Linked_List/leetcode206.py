# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if (head is None):
            return head;
        
        curNode = head;
        nodeList = [curNode];
        
        while (curNode.next):
            curNode = curNode.next;
            nodeList.append(curNode);
            
        # print(curNode);
        # print(nodeList);
        
        tail = curNode;
        
        for curIdx in range(len(nodeList) - 1 , 0 , -1):
            # print(curIdx);
            # print(nodeList[curIdx], nodeList[curIdx - 1]);
            
            nodeList[curIdx].next = nodeList[curIdx - 1];
            
        nodeList[0].next = None;
        
        return tail;
