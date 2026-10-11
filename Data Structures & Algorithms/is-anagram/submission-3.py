class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_cts = {}
        for c in s:
            if c not in s_cts:
                s_cts[c] = 1
            else:
                s_cts[c] += 1
        
        t_cts = {}
        for c in t:
            if c not in t_cts:
                t_cts[c] = 1
            else:
                t_cts[c] += 1
        
        return s_cts == t_cts
        