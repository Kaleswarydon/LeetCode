from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = []
        for i, g in enumerate(nums):
            for h in g:
                heapq.heappush(pq, (h, i))
        interval = [None] * len(nums)
        interval_len = float("inf")
        res = None
        while pq:
            val, pos = heapq.heappop(pq)
            interval[pos] = val
            if not None in interval:
                i_max, i_min = max(interval), min(interval)
                tmp = i_max - i_min
                if tmp < interval_len:
                    interval_len = tmp
                    res = [i_min, i_max]
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]  # [20,24]
    input2 = [[1,2,3],[1,2,3],[1,2,3]]  # [1,1]
    input3 = [[2,18,24,26],[0,10,12,20],[1,3,22,30]]  # [0,2]
    print(sol.smallestRange(input1))
    print(sol.smallestRange(input2))
    print(sol.smallestRange(input3))
