class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map: dict[str, int] = {}

        # Revision: can do these two loops in one go
        for i in range(len(s)):
            if s[i] in s_map:
                s_map[s[i]] += 1
            else:
                s_map[s[i]] = 1
            if t[i] in s_map:
                s_map[t[i]] -= 1
            else:
                s_map[t[i]] = -1

        for letter in s:
            if s_map[letter] != 0:
                return False
        
        return True
