INF = (10 ** 4) + 1;

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = INF;
        maxPrice = -1;
        answer = 0;
        isShareHolder = False;
        
        for curPrice in prices:
            # print(answer, isShareHolder, curPrice, minPrice, maxPrice);
            
            if (isShareHolder):
                if (maxPrice < curPrice):
                    minPrice = min(minPrice, curPrice);
                    maxPrice = curPrice;
                else:
                    answer += maxPrice - minPrice;
                    minPrice = curPrice;
                    isShareHolder = False;
            else:
                if (minPrice > curPrice):
                    minPrice = curPrice;
                    maxPrice = max(maxPrice, curPrice);
                else:
                    maxPrice = curPrice;
                    isShareHolder = True;
        
        if (isShareHolder):
            answer += maxPrice - minPrice;
        
        return answer;
