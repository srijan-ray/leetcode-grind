class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map: dict[str, int] = {}

        for letter in s:
            if letter in s_map:
                s_map[letter] += 1
            else:
                s_map[letter] = 1
        for letter in t:
            if letter not in s_map:
                return False
            if letter in s_map:
                s_map[letter] -= 1
                if s_map[letter] < 0:
                    return False

        for letter in s:
            if s_map[letter] != 0:
                return False
        
        return True
