from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = ''.join([str(ord(c) - 96) for c in s])
        for _ in range(k):
            res = sum([int(x) for x in list(str(res))])
        return res







if __name__ == '__main__':
    sol = Solution()
    input1 = "iiii", 1  # 36
    input2 = "leetcode", 2  # 6
    input3 = "zbax", 2  # 8
    print(sol.getLucky(*input1))
    print(sol.getLucky(*input2))
    print(sol.getLucky(*input3))
