class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        if (n == 0):
            return;
        
        idx2 = 0;
        
        for idx1 in range(m + n):
            if (idx2 == n):
                break;
                
            num1 = nums1[idx1];
            num2 = nums2[idx2];
            
            if (num1 > num2):
                nums1.pop();
                nums1.insert(idx1, num2);
                
                idx2 += 1;
        
        # print(idx2);
        
        while (idx2 < n):
            nums1[m + idx2] = nums2[idx2];
            
            # print(nums1, idx1);
            # print(nums2, idx2);
            
            idx2 += 1;
        
        return;
