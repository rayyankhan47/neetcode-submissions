class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def areAnagrams(s, t):
            s_counts = {}
            for char in s:
                if char not in s_counts:
                    s_counts[char] = 1
                else:
                    s_counts[char] += 1
            
            t_counts = {}
            for char in t:
                if char not in t_counts:
                    t_counts[char] = 1
                else:
                    t_counts[char] += 1
            
            return s_counts == t_counts
        
        res = []
        for st in strs[:]:
            found_group = False
            for gr in res:
                if areAnagrams(st, gr[0]):
                    found_group = True
                    gr.append(strs.pop(strs.index(st)))
                    break
            if found_group == False:
                res.append([st])
        
        return res

        

            
                

        




        


        

        

        
        
        


        

