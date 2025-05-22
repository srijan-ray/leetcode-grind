from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setOfNums = set(nums)

        length = 0
        for num in setOfNums:
            if num - 1 not in setOfNums:
                currLength = 0
                while (num + currLength) in setOfNums:
                    currLength+=1
                length = max(currLength, length)
        return length
