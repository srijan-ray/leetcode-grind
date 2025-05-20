from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out += str(len(s)) + "?" + s
        return out

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        print(s)
        while (i < len(s)):
            j = i
            while s[j] != '?':
                j += 1
            length = int(s[i:j])
            i = j + 1 
            j = i + length
            # print(s[(i + 2):j])
            out.append(s[i:j])
            i = j
        return out
