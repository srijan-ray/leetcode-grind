from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_occurances = {}
        for num in nums:
            if num not in num_occurances:
                num_occurances[num] = 1
            else:
                num_occurances[num] += 1
        
        buckets: list = [[] for x in range(len(nums) + 1)]
        
        # loop through num_occurances values
        for key in num_occurances:
            buckets[num_occurances[key]].append(key)
        
        print(buckets)

        k_ticker = k
        out = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                out.append(num)
                k_ticker -= 1
                if k_ticker == 0:
                    return out
