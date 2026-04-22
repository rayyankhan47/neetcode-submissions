class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hm = {}

        for i, num in enumerate(nums):

            other = target - num

            if other in hm:
                return [min([i, hm[other]]), max([i, hm[other]])]

            hm[num] = i
            



        
        

        