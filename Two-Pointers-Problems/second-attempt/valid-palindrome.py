class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"

        start, end = 0, len(s) - 1

        while start < end:
            while s[start] not in alphanumeric and start < len(s) - 1:
                start += 1
            while s[end] not in alphanumeric and end >= 0:
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            else:
                start += 1
                end -= 1

        return True
