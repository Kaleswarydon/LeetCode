from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None

import numpy as np
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rs = rowSum[::-1]
        cs = colSum[::-1]
        m = [[0 for x in range(len(colSum))] for y in range(len(rowSum))]
        i = 0
        j = 0
        while True:
            if i >= len(rowSum) or j >= len(colSum):
                break
            v = min(rs[-1], cs[-1])
            m[i][j] = v
            rs[-1] -= v
            cs[-1] -= v
            if not rs[-1]:
                rs.pop()
                i += 1
            if not cs[-1]:
                cs.pop()
                j += 1
        return m


if __name__ == '__main__':
    sol = Solution()
    input1 = [3,8], [4,7]
    input2 = [5,7,10], [8,6,8]
    print(sol.restoreMatrix(*input1))
    print(sol.restoreMatrix(*input2))
