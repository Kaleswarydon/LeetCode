from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def makeFancyString(self, s: str) -> str:
        curr_streak = 0
        curr_char = ''
        res = ""
        for c in s:
            if curr_char == c:
                curr_streak += 1
            else:
                curr_char = c
                curr_streak = 1
            if curr_streak >= 3 and curr_char == c:
                continue
            res += c
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = "leeetcode"  # "leetcode"
    input2 = "aaabaaaa"  # "aabaa"
    input3 = "aab"  # "aab"
    print(sol.makeFancyString(input1))
    print(sol.makeFancyString(input2))
    print(sol.makeFancyString(input3))
