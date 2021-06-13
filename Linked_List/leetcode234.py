# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        curNode = head;
        valList = [];
        
        while (curNode):
            valList.append(curNode.val);
            curNode = curNode.next;
            
        # print(valList);
        
        lp = 0;
        rp = len(valList) - 1;
        
        while (lp < rp):
            if (valList[lp] == valList[rp]):
                lp += 1;
                rp -= 1;
            else:
                return False;
            
        return True;
