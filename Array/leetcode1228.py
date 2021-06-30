import collections;

class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        answer = 0;
        diffDict = collections.defaultdict(list);
        
        for curIdx in range(len(arr) - 1):
            diffDict[arr[curIdx + 1] - arr[curIdx]].append((arr[curIdx + 1] + arr[curIdx]) // 2);
            
        # print(diffDict);
        
        for (curKey, curVal) in diffDict.items():
            if (len(curVal) == 1):
                return curVal[0];
            else:
                answer = curVal[0];
            
        return answer;
