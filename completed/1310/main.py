from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_sum = [0, arr[0]]
        for i in range(1, len(arr)):
            prefix_sum.append(arr[i] ^ prefix_sum[-1])
        res = []
        for qs, qe in queries:
            res.append(prefix_sum[qs] ^ prefix_sum[qe + 1])
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = [1,3,4,8], [[0,1],[1,2],[0,3],[3,3]]  # [2,7,14,8]
    input2 = [4,8,2,10], [[2,3],[1,3],[0,0],[0,3]]  # [8,0,4,4]
    print(sol.xorQueries(*input1))
    print(sol.xorQueries(*input2))
