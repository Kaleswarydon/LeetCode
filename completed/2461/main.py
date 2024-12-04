from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        def remove_oldest_item(o, cs):
            s.remove(nums[o])
            cs -= nums[o]
            o += 1
            return o, cs
        res = 0
        s = set()
        curr_sum = 0
        l = 0
        for r, x in enumerate(nums):
            while x in s:
                l, curr_sum = remove_oldest_item(l, curr_sum)
            s.add(x)
            curr_sum += x
            if (r - l) + 1 < k:
                continue
            res = max(res, curr_sum)
            l, curr_sum = remove_oldest_item(l, curr_sum)
            #print(l,r,s,curr_sum)
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = [1,5,4,2,9,9,9], 3  # 15
    input2 = [4,4,4], 3  # 0
    print(sol.maximumSubarraySum(*input1))
    print(sol.maximumSubarraySum(*input2))
