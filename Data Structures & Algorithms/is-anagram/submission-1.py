class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_dic = {}
        t_dic = {}

        for char in s:
            if char in s_dic:
                s_dic[char] += 1 
            else: 
                s_dic[char] = 1
        
        for char in t:
            if char in t_dic:
                t_dic[char] += 1
            else:
                t_dic[char] = 1

        return s_dic == t_dic 
                 

        