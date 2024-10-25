from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        col_len = len(points)
        row_len = len(points[0])
        if col_len == 1:
            return max(points[0])
        if row_len == 1:
            return sum([r[0] for r in points])
        tmp = [0 for _ in range(row_len)]
        res = 0
        for i in range(1, col_len):
            tmp[0] = points[i - 1][0]
            tmp[-1] = points[i - 1][-1]
            for j in range(1, row_len):
                tmp[j] = max(tmp[j], points[i - 1][j], tmp[j - 1] - 1)
                tmp[row_len - j - 1] = max(tmp[row_len - j - 1], points[i - 1][row_len - j - 1], tmp[row_len - j] - 1)
            for k in range(len(tmp)):
                points[i][k] += tmp[k]
                res = max(res, points[i][k])
        return res


if __name__ == '__main__':
    sol = Solution()
    input1 = [[1,2,3],[1,5,1],[3,1,1]]  # 9
    input2 = [[1,5],[2,3],[4,2]]  # 11
    input3 = [[10]]  # 10
    input4 = [[2,4,0,5,5],[0,5,4,2,5],[2,0,2,3,1],[3,0,5,5,2]]  # 17
    print(sol.maxPoints(input1))
    print(sol.maxPoints(input2))
    print(sol.maxPoints(input3))
    print(sol.maxPoints(input4))
