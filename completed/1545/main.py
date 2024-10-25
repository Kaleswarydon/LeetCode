from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def __init__(self):
        self.cache = {}

    def get_sn(self, n: int) -> str:
        if n > 1:
            if n - 1 not in self.cache:
                s_prev = self.get_sn(n - 1)
            else:
                s_prev = self.cache[n - 1]
            s_prev_inv = ''.join(["1" if x == "0" else "0" for x in s_prev])
            self.cache[n] = s_prev + "1" + s_prev_inv[::-1]
            return s_prev + "1" + s_prev_inv[::-1]
        else:
            return "0"

    def findKthBit(self, n: int, k: int) -> str:
        return self.get_sn(n)[k - 1]


if __name__ == '__main__':
    # S1 = "0"
    # S2 = "011"
    # S3 = "0111001"
    # S4 = "011100110110001"
    sol = Solution()
    input1 = 3, 1  # 0
    input2 = 4, 11  # 1
    print(sol.findKthBit(*input1))
    print(sol.findKthBit(*input2))
