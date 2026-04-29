class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        freq = sorted(list(counts), key=lambda x: counts[x], reverse=True)

        return freq[:k]
        
        