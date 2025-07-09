from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack: list[tuple[int, int]] = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                prevIdx, _ = stack.pop()
                res[prevIdx] =  i - prevIdx
            stack.append(( i, t ))

        return res
