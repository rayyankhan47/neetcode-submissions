class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hm = defaultdict(list)

        
        # one-hot encoding, O(26mn), m = len(strs), n = avg(len(char) for char in str for str in strs)
        for str in strs:
            count = [0] * 26
            for char in str:
                count[ord(char) - ord('a')] += 1
            
            hm[tuple(count)].append(str)
        
        # return all the lists
        return list(hm.values())
            
            
            
            



            
            
        

        



        

        

            
                

        




        


        

        

        
        
        


        

