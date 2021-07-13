class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        (longestKey, longestDuration) = (keysPressed[0], releaseTimes[0]);
        
        for releaseIdx in range(1, len(releaseTimes)):
            curReleaseTime = releaseTimes[releaseIdx] - releaseTimes[releaseIdx - 1];
            
            if (longestDuration < curReleaseTime):
                (longestKey, longestDuration) = (keysPressed[releaseIdx], curReleaseTime);
            elif ((longestDuration == curReleaseTime) and (ord(longestKey) < ord(keysPressed[releaseIdx]))):
                (longestKey, longestDuration) = (keysPressed[releaseIdx], curReleaseTime);
                
        return longestKey;
