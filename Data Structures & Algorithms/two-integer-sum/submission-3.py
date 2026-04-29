class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hm = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in hm:
                return [min(i, hm[comp]), max(i, hm[comp])]
            hm[num] = i
        



        
        

        