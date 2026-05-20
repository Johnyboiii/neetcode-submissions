class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        for char in nums:
            if nums.count(char) > 1:
                return True
        
        return False
