from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        r = sum(nums) % p
        if not r:
            return 0
        ps = defaultdict(int)
        ps[0] = -1
        curr_sum = 0
        res = len(nums)
        for i, x in enumerate(nums):
            curr_sum = (curr_sum + x) % p
            tmp_r = (curr_sum - r) % p
            if tmp_r in ps:
                res = min(res, i - ps[tmp_r])
            ps[curr_sum] = i
        if res == len(nums):
            return -1
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = [3,1,4,2], 6  # 1
    input2 = [6,3,5,2], 9  # 2
    input3 = [1,2,3], 3  # 0
    print(sol.minSubarray(*input1))
    print(sol.minSubarray(*input2))
    print(sol.minSubarray(*input3))
