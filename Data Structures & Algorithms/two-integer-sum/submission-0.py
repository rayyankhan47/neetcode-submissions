class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hm = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in hm:
                return [min(i, hm[comp]), max(i, hm[comp])]
            hm[num] = i
        
        """
        The reason as to why we add num to hm only if the comp in hm condition fails is because its possible that num's comp is num itself (e.g. target = num * 2).
        If we did hm[num] = i before the condition in this situation, then we'd return the same index twice (which is never the desired solution from the nature of this problem.)
        """