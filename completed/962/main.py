from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        mr = [nums[-1]]
        for i in range(len(nums) - 2, -1, -1):
            mr.append(max(nums[i], mr[-1]))
        res = 0
        ptr_lo = 0
        for ptr_hi in range(1, len(nums)):
            if nums[ptr_lo] <= mr[len(nums) - 1 - ptr_hi]:
                res = max(res, ptr_hi - ptr_lo)
            else:
                ptr_lo += 1
                ptr_hi -= 1
        return res

if __name__ == '__main__':
    sol = Solution()
    input0 = [6,0,8,2,1,6]  # 5
    input1 = [6,0,8,2,1,5]  # 4
    input2 = [9,8,1,0,1,9,4,0,4,1]  # 7
    print(sol.maxWidthRamp(input0))
    print(sol.maxWidthRamp(input1))
    print(sol.maxWidthRamp(input2))
