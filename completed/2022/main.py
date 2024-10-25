from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if not len(original) / m == n:
            return []
        res = []
        for i in range(m):
            tmp = []
            for j in range(n):
                tmp.append(original[(i * n) + j])
            res.append(tmp)
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = [1,2,3,4], 2, 2  # [[1,2],[3,4]]
    input2 = [1,2,3], 1, 3  # [[1,2,3]]
    input3 = [1,2], 1, 1  # []
    print(sol.construct2DArray(*input1))
    print(sol.construct2DArray(*input2))
    print(sol.construct2DArray(*input3))
