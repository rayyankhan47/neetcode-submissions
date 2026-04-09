class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        """
            1. take counts of each w/ hm's
            2. compare hm's
        """

        # counts of s
        hm_s = {}
        for char in s:
            if char not in hm_s:
                hm_s[char] = 1
            else:
                hm_s[char] += 1
        
        # counts of t
        hm_t = {}
        for char in t:
            if char not in hm_t:
                hm_t[char] = 1
            else:
                hm_t[char] += 1

        return hm_s == hm_t

        
        