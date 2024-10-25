from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        deq_min = deque()
        deq_max = deque()
        res = 0
        ptr_lo = 0
        for ptr_hi in range(len(nums)):
            while deq_min and deq_min[-1][1] >= nums[ptr_hi]:
                deq_min.pop()
            deq_min.append((ptr_hi, nums[ptr_hi]))
            while deq_max and deq_max[-1][1] <= nums[ptr_hi]:
                deq_max.pop()
            deq_max.append((ptr_hi, nums[ptr_hi]))
            if deq_max[0][1] - deq_min[0][1] > limit:
                ptr_lo += 1
                if ptr_lo > deq_min[0][0]:
                    deq_min.popleft()
                if ptr_lo > deq_max[0][0]:
                    deq_max.popleft()
            else:
                tmp = (ptr_hi - ptr_lo) + 1
                if res < tmp:
                    res = tmp
        return res




if __name__ == '__main__':
    sol = Solution()
    input1 = [8,2,4,7], 4  # 2
    input2 = [10,1,2,4,7,2], 5  # 4
    input3 = [4,2,2,2,4,4,2,2], 0  # 3
    input4 = [24,12,71,33,5,87,10,11,3,58,2,97,97,36,32,35,15,80,24,45,38,9,22,21,33,68,22,85,35,83,92,38,59,90,42,64,61,15,4,40,50,44,54,25,34,14,33,94,66,27,78,56,3,29,3,51,19,5,93,21,58,91,65,87,55,70,29,81,89,67,58,29,68,84,4,51,87,74,42,85,81,55,8,95,39], 87  # 25
    print(sol.longestSubarray(*input1))
    print(sol.longestSubarray(*input2))
    print(sol.longestSubarray(*input3))
    print(sol.longestSubarray(*input4))
