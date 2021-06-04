class Solution:
    def isPalindrome(self, s: str) -> bool:
        answer = True;
        sLen = len(s);
        lp = 0;
        rp = sLen - 1;
        
        while (lp < rp):
            while ((lp < sLen) and (not s[lp].isalnum())):
                lp += 1;
                
            while ((rp >= 0) and (not s[rp].isalnum())):
                rp -= 1;
            
            # print(lp, rp, s[lp].lower(), s[rp].lower());
            
            if (lp >= rp):
                break;
            
            if (s[lp].lower() != s[rp].lower()):
                answer = False;
                
                break;
            
            lp += 1;
            rp -= 1;
        
        return answer;
