from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def dummy(self, nums):
        ptr_lo = 0
        ptr_hi = len(nums) - 1
        i = 0
        while i <= ptr_hi:
            if nums[i] == 0:
                nums[i] = nums[ptr_lo]
                nums[ptr_lo] = 0
                ptr_lo += 1
            if nums[i] == 2:
                nums[i] = nums[ptr_hi]
                nums[ptr_hi] = 2
                ptr_hi -= 1
                continue
            i += 1
        print(nums)

if __name__ == '__main__':
    sol = Solution()
    input1 = [2,0,2,1,1,0]
    input2 = [2,0,1]
    input3 = [2,0,2,1,1,0,2,0,2,1,1,0,2,0,2,1,1,0,2,0,2,1,1,0]
    input4 = [1]
    input5 = [1,1]
    input6 = [0,0,1]
    print(sol.dummy(input1))
    print(sol.dummy(input2))
    print(sol.dummy(input3))
    print(sol.dummy(input4))
    print(sol.dummy(input5))
    print(sol.dummy(input6))

