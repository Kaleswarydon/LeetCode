from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def dummy(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pq = []
        for x, y in zip(profits, capital):
            heapq.heappush(pq, (y, x))
        pq2 = []
        for i in range(k):
            while pq and pq[0][0] <= w:
                tmp = heapq.heappop(pq)
                heapq.heappush(pq2, -tmp[-1])
            if pq2:
                w -= heapq.heappop(pq2)
        return w


if __name__ == '__main__':
    sol = Solution()
    input1 = 2, 0, [1,2,3], [0,1,1] # 4
    input2 = 3, 0, [1,2,3], [0,1,2] # 6
    input3 = 1, 2, [1,2,3], [1,1,2] # 5
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
    print(sol.dummy(*input3))
