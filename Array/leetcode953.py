def cmpWord(word1 : str, word2 : str, orderDict : dict) -> bool:
    (chIdx1, chIdx2) = (0, 0);
    
    while ((chIdx1 < len(word1)) and (chIdx2 < len(word2))):
        isDifferent = False;
        (order1, order2) = (orderDict[word1[chIdx1]], orderDict[word2[chIdx2]]);
        
        # print(orderDict[word1[chIdx1]], orderDict[word2[chIdx2]]);
        
        if (order1 != order2):
            return (order1 < order2);
            
        (chIdx1, chIdx2) = (chIdx1 + 1, chIdx2 + 1);
        
    return (len(word1) <= len(word2));

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderDict = {k : v for (v, k) in enumerate(order)};
        
        # print(orderDict);
        
        for wordIdx in range(len(words) - 1):
            if (not cmpWord(words[wordIdx], words[wordIdx + 1], orderDict)):
                return False;
            
        return True;
