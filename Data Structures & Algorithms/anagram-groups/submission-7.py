class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import defaultdict

        def count(st):
            hm = {}
            for c in st:
                if c not in hm:
                    hm[c] = 1
                else:
                    hm[c] += 1
            return hm
        
        # the goal is to classify the strings into
        # sub-lists wrt their count hm's.

        counts_to_strs = defaultdict(list)

        for st in strs:
            hm_key = tuple(sorted(count(st).items()))
            counts_to_strs[hm_key].append(st)
        
        anagram_groups = []
        for anagram_group in counts_to_strs.values():
            anagram_groups.append(anagram_group)
        
        return anagram_groups



        

        
        
        