class Solution:
    def validPalindrome(self, s: str) -> bool:
        (leftIdx, rightIdx) = (0, len(s) - 1);
        
        while (leftIdx < rightIdx):
            if (s[leftIdx] != s[rightIdx]):
                # print(s[leftIdx : rightIdx], ''.join(list(reversed(s[leftIdx : rightIdx]))));
                # print(s[leftIdx + 1 : rightIdx + 1], ''.join(list(reversed(s[leftIdx + 1 : rightIdx + 1]))));
                
                return ((s[leftIdx : rightIdx] == ''.join(list(reversed(s[leftIdx : rightIdx])))) or 
                        (s[leftIdx + 1 : rightIdx + 1] == ''.join(list(reversed(s[leftIdx + 1 : rightIdx + 1])))));
                
            (leftIdx, rightIdx) = (leftIdx + 1, rightIdx - 1);
            
        return True;
