class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            # 1. Skip non-alphanumeric from left 
            while left < right and not s[left].isalnum():
                left += 1
            # 2. Skip non-alphanumeric from right 
            while left < right and not s[right].isalnum():
                right -= 1
            
            # 3. Compare lowercase characters 
            if s[left].lower() != s[right].lower():
                return False
            
            # 4. Move pointers inward
            left += 1
            right -= 1
            
        return True