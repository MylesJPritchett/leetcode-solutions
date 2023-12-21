class Solution:
    def isPalindrome(self, s: str) -> bool:
        input = ''.join(filter(str.isalnum, s)).lower()
        if input == input [::-1]:
            return True
        else:
            return False