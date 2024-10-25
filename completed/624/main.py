from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        mi = arrays[0][0]
        ma = arrays[0][-1]
        for a in arrays[1:]:
            res = max(res, ma - a[0], a[-1] - mi)
            mi = min(mi, a[0])
            ma = max(ma, a[-1])
        return res


if __name__ == '__main__':
    sol = Solution()
    input1 = [[1,2,3],[4,5],[1,2,3]]  # 4
    input2 = [[1],[1]]  # 0
    input3 = [[1,4],[0,5]]  # 4
    print(sol.maxDistance(input1))
    print(sol.maxDistance(input2))
    print(sol.maxDistance(input3))
