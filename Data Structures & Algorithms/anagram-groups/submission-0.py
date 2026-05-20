class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = {}

        for n in strs:
            if ''.join(sorted(n)) in seen:
                seen[''.join(sorted(n))].append(n)
            else:
                seen[''.join(sorted(n))] = [n]
        
        return list(seen.values()) #gets all the items from the dict