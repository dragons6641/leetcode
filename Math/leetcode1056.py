VALID_DIGIT_DICT = {'6' : '9', '9' : '6'}
INVALID_DIGIT_LIST = ['2', '3', '4', '5', '7'];

class Solution:
    def confusingNumber(self, n: int) -> bool:
        isDifferent = False;
        orgStr = str(n);
        rotatedStr = "";
        
        for curCh in orgStr:
            if (curCh in INVALID_DIGIT_LIST):
                return False;

            if (curCh in VALID_DIGIT_DICT.keys()):
                rotatedStr += VALID_DIGIT_DICT[curCh];
            else:
                rotatedStr += curCh;
        
        # print(rotatedStr[ : : -1]);
        
        return (orgStr != rotatedStr[ : : -1]);
