from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def strangePrinter(self, s: str) -> int:
        def helper(start, end):
            if start > end:
                return 0
            if (start, end) in cache:
                return cache[(start, end)]
            res = helper(start, end - 1) + 1
            for mid in range(start, end):
                if s[mid] == s[end]:
                    res = min(res, helper(start, mid) + helper(mid + 1, end - 1))
            cache[(start, end)] = res
            return res
        cache = {}
        return helper(0, len(s) - 1)

if __name__ == '__main__':
    sol = Solution()
    input1 = "aaabbb"  # 2
    input2 = "aba"  # 2
    input3 = "abcab"  # 4
    input4 = "abcabc"  # 5
    print(sol.strangePrinter(input1))
    print(sol.strangePrinter(input2))
    print(sol.strangePrinter(input3))
    print(sol.strangePrinter(input4))
