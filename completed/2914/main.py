from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def minChanges(self, s: str) -> int:
        res = 0
        for x in [(s[i:i+2]) for i in range(0, len(s), 2)]:
            res += len(set(x)) - 1
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = "1001"  # 2
    input2 = "10"  # 1
    input3 = "0000"  # 0
    print(sol.minChanges(input1))
    print(sol.minChanges(input2))
    print(sol.minChanges(input3))
