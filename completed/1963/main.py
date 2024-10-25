from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def minSwaps(self, s: str) -> int:
        s = list(s)
        res = 0
        curr_last_opening = len(s) - 1
        o = 0  # opening brackets
        c = 0  # closing brackets
        for i in range(len(s)):
            if s[i] == '[':
                o += 1
            else:
                c += 1
            if c > o:
                while s[curr_last_opening] != '[':
                    curr_last_opening -= 1
                tmp = s[i]
                s[i] = s[curr_last_opening]
                s[curr_last_opening] = tmp
                o += 1
                c -= 1
                res += 1
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = "][]["  # 1
    input2 = "]]][[["  # 2
    input3 = "[]"  # 0
    print(sol.minSwaps(input1))
    print(sol.minSwaps(input2))
    print(sol.minSwaps(input3))
