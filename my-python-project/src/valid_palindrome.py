class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        # time complexity = O(n)

        # for regex match complexity is O(n*m) m is length of pattern and n is length of string
        left, right = 0, len(filtered_chars) - 1
        
        while left < right:
            if filtered_chars[left] != filtered_chars[right]:
                return False
            left += 1
            right -= 1
            
        return True
    
obj = Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))  # Expected output is True