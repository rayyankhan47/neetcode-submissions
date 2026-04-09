class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def areAnagrams(s, t):

            hm1 = {}
            for char in s:
                if char not in hm1:
                    hm1[char] = 1
                else:
                    hm1[char] += 1
            hm2 = {}
            for char in t:
                if char not in hm2:
                    hm2[char] = 1
                else:
                    hm2[char] += 1

            return hm1 == hm2
        
        res = []

        for st in strs:
            found_st_gr = False
            for st_gr in res:
                if areAnagrams(st, st_gr[0]):
                    st_gr.append(st)
                    found_st_gr = True
                    break
            if found_st_gr == False:
                res.append([st])
        
        return res

