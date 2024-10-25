from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return bin(start ^ goal)[2:].count('1')


if __name__ == '__main__':
    sol = Solution()
    input1 = 10, 7  # 3
    input2 = 3, 4  # 3
    print(sol.minBitFlips(*input1))
    print(sol.minBitFlips(*input2))
