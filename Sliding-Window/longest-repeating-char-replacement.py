class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count: dict[str, int] = {}

        right = 0
        res = 0
        for left in range(0, len(s)):
            count[s[left]] = 1 + count.get(s[left], 0)

            while abs(right - left) + 1 - max(count.values())> k:
                count[s[right]] -= 1
                right += 1

            res = max(res, abs(right - left) + 1)
        return res
