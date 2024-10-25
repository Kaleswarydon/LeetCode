from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [0 if not x % 2 else 1 for x in nums]
        ptr_lo = 0
        odds = 0
        res = 0
        prev_subarrays = 0
        for ptr_hi in range(len(nums)):
            if nums[ptr_hi]:
                odds += 1
                prev_subarrays = 0
            while odds == k:
                if nums[ptr_lo]:
                    odds -= 1
                ptr_lo += 1
                prev_subarrays += 1
            res += prev_subarrays
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = [1,1,2,1,1], 3  # 2
    input2 = [2,4,6], 1  # 0
    input3 = [2,2,2,1,2,2,1,2,2,2], 2  # 16
    print(sol.numberOfSubarrays(*input1))
    print(sol.numberOfSubarrays(*input2))
    print(sol.numberOfSubarrays(*input3))
