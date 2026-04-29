class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hm_s = {}
        for char in s:
            if char in hm_s:
                hm_s[char] += 1
            else:
                hm_s[char] = 1
        
        hm_t = {}
        for char in t:
            if char in hm_t:
                hm_t[char] += 1
            else:
                hm_t[char] = 1
        
        return hm_s == hm_t
        
        