from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res = 0
        global_min = float("inf")
        even_odd_counter = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                tmp = abs(matrix[i][j])
                even_odd_counter ^= int(matrix[i][j] < 0)
                res += tmp
                if tmp < global_min:
                    global_min = tmp
        #print(res, global_min, even_odd_counter)
        return res - (even_odd_counter * (global_min * 2))

if __name__ == '__main__':
    sol = Solution()
    input1 = [[1,-1],[-1,1]]  # 4
    input2 = [[1,2,3],[-1,-2,-3],[1,2,3]]  # 16
    print(sol.maxMatrixSum(input1))
    print(sol.maxMatrixSum(input2))
