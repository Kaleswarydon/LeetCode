from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def dummy(self, n: int, time: int) -> int:
        cycles, remaining_time = divmod(time, (n * 2) - 2)
        first_half, remaining_time2 = divmod(remaining_time, n)
        if first_half % 2:
            return n - (remaining_time2 + 1)
        else:
            return remaining_time2 + 1

if __name__ == '__main__':
    sol = Solution()
    input1 = 4, 5  # 2
    input2 = 3, 2  # 3
    input3 = 3, 15  # 2
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
    print(sol.dummy(*input3))
