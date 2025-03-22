class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        alphanumeric_chars = ''.join(char.lower() for char in s if char.isalnum())
        
        return alphanumeric_chars == alphanumeric_chars[::-1]