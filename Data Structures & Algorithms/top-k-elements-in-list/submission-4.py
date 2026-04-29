class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = defaultdict(int)
        for num in nums: # O(n)
            counts[num] += 1

        # O(nlogn)
        freq = sorted(list(counts), key=lambda x: counts[x], reverse=True)

        return freq[:k]
        
        