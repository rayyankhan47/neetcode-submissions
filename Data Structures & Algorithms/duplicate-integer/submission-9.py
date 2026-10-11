class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_unique = set(nums)
        return len(nums) != len(nums_unique)
        