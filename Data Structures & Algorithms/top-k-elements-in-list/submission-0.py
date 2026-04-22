class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hm = {}

        for num in nums:
            if num not in hm:
                hm[num] = 1
            else:
                hm[num] += 1
        
        sorted_counts = sorted(hm.keys(), key=lambda x: hm[x], reverse=True)

        return sorted_counts[:k]

        
        