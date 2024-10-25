from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        window_size = sum(nums)
        ones_in_current_window = sum(nums[:window_size])
        ptr_lo = 0
        ptr_hi = window_size - 1
        res = window_size - ones_in_current_window
        #print(ptr_lo, ptr_hi, ones_in_current_window, res)
        for i in range(1, len(nums)):
            ptr_hi += 1
            if ptr_hi > len(nums) - 1:
                ptr_hi = ptr_hi - len(nums)
            ones_in_current_window += nums[ptr_hi] - nums[ptr_lo]
            ptr_lo += 1
            #print(ptr_lo, ptr_hi, ones_in_current_window)
            res = min(res, window_size-ones_in_current_window)
        return res



if __name__ == '__main__':
    sol = Solution()
    input1 = [0,1,0,1,1,0,0]  # 1
    input2 = [0,1,1,1,0,0,1,1,0]  # 2
    input3 = [1,1,0,0,1]  # 0
    input4 = [1,1,1,0,0,1,0,1,1,0]  # 1
    print(sol.minSwaps(input1))
    print(sol.minSwaps(input2))
    print(sol.minSwaps(input3))
    print(sol.minSwaps(input4))
