class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)

        # 1. prefix pass: calcualte products to the left
        prefix = 1 
        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]

        # 2. suffix pass: multiply by products to the right 
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res 
        