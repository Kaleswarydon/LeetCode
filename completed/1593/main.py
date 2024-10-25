from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def rec(start: int, current_substrs: set):
            if start == len(s):
                return 0
            res = 0
            for stop in range(start, len(s)):
                substr = s[start:stop+1]
                if substr not in current_substrs:
                    current_substrs.add(substr)
                    res = max(res, rec(stop + 1, current_substrs) + 1)
                    current_substrs.remove(substr)
            return res
        return rec(0, set())

if __name__ == '__main__':
    sol = Solution()
    input1 = "ababccc"  # 5
    input2 = "aba"  # 2
    input3 = "aa"  # 1
    input4 = "wwwzfvedwfvhsww"  # 11
    print(sol.maxUniqueSplit(input1))
    print(sol.maxUniqueSplit(input2))
    print(sol.maxUniqueSplit(input3))
    print(sol.maxUniqueSplit(input4))
