from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List
import math

class Solution:
    def dummy(self, c: int) -> bool:
        ptr_lo = 0
        ptr_hi = int(math.sqrt(c))
        while ptr_lo <= ptr_hi:
            tmp = (ptr_lo ** 2) + (ptr_hi ** 2)
            if tmp < c:
                ptr_lo += 1
            elif tmp > c:
                ptr_hi -= 1
            else:
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    input1 = 5 # 1
    input2 = 3 # 0
    input3 = 4 # 1
    input4 = 2 # 1
    print(sol.dummy(input1))
    print(sol.dummy(input2))
    print(sol.dummy(input3))
    print(sol.dummy(input4))
