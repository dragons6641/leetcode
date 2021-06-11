STR_LEN = 32;

class Solution:
    def reverseBits(self, n: int) -> int:
        answer = int(''.join(list(reversed(list(str(bin(n))[2:].zfill(STR_LEN))))), 2);
        
        # print(answer);
        
        return answer;
