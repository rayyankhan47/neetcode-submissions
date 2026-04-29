class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        bucket_sort = [[] for _ in range(n+1)]

        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        for num, count in counts.items():
            bucket_sort[count].append(num)
        
        res = []

        for frequency in bucket_sort[::-1]:
            if len(res) == k:
                return res
            for num in frequency:
                if len(res) == k:
                    return res
                res.append(num)
        


        
        