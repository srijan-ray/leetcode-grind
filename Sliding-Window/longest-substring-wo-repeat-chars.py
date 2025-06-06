class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0

        seen: set[str] = set()
        maxLen = 0
        currLen = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                currLen -= 1
            seen.add(s[right])
            currLen += 1
            maxLen = max(maxLen, currLen)
        
        return maxLen
