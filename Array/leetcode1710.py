class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        (answer, boxCnt) = (0, 0);
        
        for (numberOfBoxes, numberOfUnitsPerBox) in sorted(boxTypes, key = lambda k : -k[1]):
            if (boxCnt + numberOfBoxes >= truckSize):
                (answer, boxCnt) = (answer + ((truckSize - boxCnt) * numberOfUnitsPerBox), truckSize);
                break;
                
            (answer, boxCnt) = (answer + (numberOfBoxes * numberOfUnitsPerBox), boxCnt + numberOfBoxes);
        
        return answer;
