from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        def check_before(x, y):
            return min(res_mat[x][y - 1], res_mat[x - 1][y - 1], res_mat[x - 1][y])
        res_mat = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        res = 0
        for i in range(1, len(res_mat)):
            for j in range(1, len(res_mat[0])):
                if matrix[i-1][j-1]:
                    tmp = 1 + check_before(i - 1, j  -1)
                    res_mat[i - 1][j - 1] = tmp
                    res += tmp
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]  # 15
    input2 = [[1,0,1],[1,1,0],[1,1,0]]  # 7
    print(sol.countSquares(input1))
    print(sol.countSquares(input2))
