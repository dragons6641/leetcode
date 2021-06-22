import collections;

class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if (len(sentence1) != len(sentence2)):
            return False;
        
        similarDict = collections.defaultdict(list);
        
        for (word1, word2) in similarPairs:
            similarDict[word1].append(word2);
            similarDict[word2].append(word1);
        
        for (word1, word2) in zip(sentence1, sentence2):
            if ((word1 != word2) and (word1 not in similarDict[word2])):
                return False;
            
        return True;
