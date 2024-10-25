from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def minimumSteps(self, s: str) -> int:
        res = 0
        tmp_cntr = 0
        for x in s[::-1]:
            if x == '1':
                res += tmp_cntr
            else:
                tmp_cntr += 1
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = "101"  # 1
    input2 = "100"  # 2
    input3 = "0111"  # 0
    input4 = "11000111"  # 6
    print(sol.minimumSteps(input1))
    print(sol.minimumSteps(input2))
    print(sol.minimumSteps(input3))
    print(sol.minimumSteps(input4))
