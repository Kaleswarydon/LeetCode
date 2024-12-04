from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        if n == 1:
            return x
        n = bin(n-1)[2:]
        x = bin(x)[2:]
        print(n,x)
        res = ""
        for b in x[::-1]:
            if b == '0' and n:
                res += n[-1]
                n = n[:-1]
            else:
                res += b
        print(res, n)
        res = n + res[::-1]
        return int(res, 2)


if __name__ == '__main__':
    sol = Solution()
    input1 = 3, 4  # 6
    input2 = 2, 7  # 15
    input3 = 3, 2  # 6
    input4 = 3, 1  # 5
    input5 = 2, 4  #
    print(sol.minEnd(*input1))
    print(sol.minEnd(*input2))
    print(sol.minEnd(*input3))
    print(sol.minEnd(*input4))
    print(sol.minEnd(*input5))
