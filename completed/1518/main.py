from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def dummy(self, numBottles: int, numExchange: int) -> int:
        res = 0
        tmp = -1
        while tmp:
            tmp, numBottles = divmod(numBottles, numExchange)
            res += tmp * numExchange
            numBottles += tmp
        res += numBottles
        return res


if __name__ == '__main__':
    sol = Solution()
    input1 = 9, 3  # 13
    input2 = 15, 4  # 19
    input3 = 15, 8  # 17
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
    print(sol.dummy(*input3))
