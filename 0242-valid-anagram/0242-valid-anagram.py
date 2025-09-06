class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countDict = {}

        for c in s:
            if c in countDict:
                countDict[c] += 1
            else:
                countDict[c] = 1
        
        for c in t:
            if c not in countDict or countDict[c] == 0:
                return False
            else:
                countDict[c] -= 1
        
        return True