class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False

        countS, countT = {}, {}

        for n in s: 
            if  n in countS:
                countS[n] += 1
            else:
                countS[n] = 1
        
        for n in t:
            if n in countT:
                countT[n] += 1
            else:
                countT[n] = 1

        return countS == countT 
        