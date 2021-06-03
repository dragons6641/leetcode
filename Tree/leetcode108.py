# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def makeBST(nums, leftIdx, rightIdx) -> TreeNode:
    if (leftIdx == rightIdx):
        return TreeNode(val = nums[leftIdx], left = None, right = None);
    elif (leftIdx > rightIdx):
        return None;
    
    midIdx = (leftIdx + rightIdx + 1) // 2;
    
    subTree = TreeNode(val = nums[midIdx], left = None, right = None);
    subTree.left = makeBST(nums = nums, leftIdx = leftIdx, rightIdx = midIdx - 1);
    subTree.right = makeBST(nums = nums, leftIdx = midIdx + 1, rightIdx = rightIdx);
    
    return subTree;

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # print(nums);
        
        leftIdx = 0;
        rightIdx = len(nums) - 1;
        midIdx = (leftIdx + rightIdx + 1) // 2;
        
        answer = makeBST(nums = nums, leftIdx = midIdx, rightIdx = midIdx);
        answer.left = makeBST(nums = nums, leftIdx = leftIdx, rightIdx = midIdx - 1);
        answer.right = makeBST(nums = nums, leftIdx = midIdx + 1, rightIdx = rightIdx);
        
        # print(answer);
        
        return answer;
