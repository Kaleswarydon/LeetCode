from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        def helper(a, i, m):
            if (a, i, m) in cache:
                return cache.get((a, i, m))
            if i == len(piles):
                return 0
            res = 0 if a else float("inf")
            stones = 0
            for x in range(1, (2 * m) + 1):
                tmp = i + x - 1
                if tmp == len(piles):
                    break
                stones += piles[tmp]
                if a:
                    res = max(res, stones + helper(not a, i + x, max(m, x)))
                else:
                    res = min(res, helper(not a, i + x, max(m, x)))
            cache[(a, i, m)] = res
            return res
        cache = {}
        return helper(1, 0, 1)

if __name__ == '__main__':
    sol = Solution()
    input1 = [2,7,9,4,4]  # 10
    input2 = [1,2,3,4,5,100]  # 104
    print(sol.stoneGameII(input1))
    print(sol.stoneGameII(input2))
