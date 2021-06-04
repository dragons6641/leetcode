INF = (10 ** 4) + 1;

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = INF;
        maxPrice = -1;
        answer = 0;
        
        for curPrice in prices:
            # print(answer, curPrice, minPrice, maxPrice);
            
            if (minPrice > curPrice):
                if (minPrice < INF):
                    # print("NOT INF");
                    
                    answer = max(answer, maxPrice - minPrice);
                
                minPrice = curPrice;
                maxPrice = curPrice;
            else:
                maxPrice = max(maxPrice, curPrice);
                
        answer = max(answer, maxPrice - minPrice);
        
        return answer;
