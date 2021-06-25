import collections;

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        answer = [];
        highFiveDict = collections.defaultdict(list);
        
        for (curID, curScore) in items:
            highFiveDict[curID].append(curScore);
            
        # print(highFiveDict);
        
        for (curKey, curVal) in highFiveDict.items():
            answer.append([curKey, sum(sorted(curVal, reverse = True)[ : 5]) // 5]);
            
        answer.sort(key = lambda k : k[0]);
        
        # print(answer);
        
        return answer;
