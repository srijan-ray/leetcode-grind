from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(num_open: int, num_closed: int, curr_str: str):
            if num_open == num_closed == n:
                res.append(curr_str)
                return

            if num_closed < num_open:
                backtrack(num_open, num_closed + 1, curr_str + ")")

            if num_open < n:
                backtrack(num_open + 1, num_closed, curr_str + "(")

        backtrack(0,0,"")
        return res
