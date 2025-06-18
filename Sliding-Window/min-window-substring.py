class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        if len(t) > len(s):
            return ""

        countT: dict[str, int] = {}
        window: dict[str, int] = {}

        left, right = 0, 0
        res = [left, right]
        minWindow = float('inf')
        have = 0

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        need = len(countT)

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            
            if have == need:
                while have >= need:
                    if minWindow > r - left + 1:
                        minWindow = r - left + 1
                        res = [left, r]

                    window[s[left]] -= 1
                    if s[left] in countT and window[s[left]] < countT[s[left]]:
                        have -= 1
                    
                    left += 1
        
        return s[res[0]:res[1]+1] if minWindow != float('inf') else ""
