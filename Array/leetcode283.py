class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zeroIdx = 0;
        
        for curIdx in range(len(nums)):
            if (nums[curIdx] != 0):
                nums[curIdx], nums[zeroIdx] = nums[zeroIdx], nums[curIdx];
                zeroIdx += 1;
        
        return None;
