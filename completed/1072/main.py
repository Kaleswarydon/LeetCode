from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        d = defaultdict(int)
        for row in matrix:
            t = row[0]
            tmp = ""
            for item in row:
                if item == t:
                    tmp += 'a'
                else:
                    tmp += 'b'
            d[tmp] += 1
        return max(d.values())


if __name__ == '__main__':
    sol = Solution()
    input1 = [[0,1],[1,1]]  # 1
    input2 = [[0,1],[1,0]]  # 2
    input3 = [[0,0,0],[0,0,1],[1,1,0]]  # 2
    print(sol.maxEqualRowsAfterFlips(input1))
    print(sol.maxEqualRowsAfterFlips(input2))
    print(sol.maxEqualRowsAfterFlips(input3))
