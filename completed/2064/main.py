from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l = 1
        r = max(quantities)
        if n == len(quantities):
            return r
        if n > sum(quantities):
            return 1
        while l <= r:
            m = (l + r) // 2
            needed_shops = 0
            for q in quantities:
                di, mo = divmod(q, m)
                needed_shops += di + int(bool(mo))
            if needed_shops > n:
                l = m + 1
            else:
                r = m - 1
        return l

if __name__ == '__main__':
    sol = Solution()
    input1 = 6, [11,6]  # 3
    input2 = 7, [15,10,10]  # 5
    input3 = 1, [100000]  # 100000
    input4 = 15, [18,28,11,8,22,16,24,18,26,26,21,24]  # 24
    input5 = 19, [26,1,11,7,8,5,18,16,7,21,1,10,30,30]  # 16
    print(sol.minimizedMaximum(*input1))
    print(sol.minimizedMaximum(*input2))
    print(sol.minimizedMaximum(*input3))
    print(sol.minimizedMaximum(*input4))
    print(sol.minimizedMaximum(*input5))
