from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:  # josephus problem
        if n == 1:
            return 1
        return ((self.findTheWinner(n - 1, k) + k - 1) % n) + 1

if __name__ == '__main__':
    sol = Solution()
    input1 = 5, 2  # 3
    input2 = 6, 5  # 1
    print(sol.findTheWinner(*input1))
    print(sol.findTheWinner(*input2))
