from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def compressedString(self, word: str) -> str:
        res = ""
        curr_char = word[0]
        curr_streak = 0
        for c in word:
            if (not curr_char or curr_char == c) and curr_streak <= 8:
                curr_streak += 1
            else:
                res += str(curr_streak) + curr_char
                curr_char = c
                curr_streak = 1
        return res + str(curr_streak) + curr_char


if __name__ == '__main__':
    sol = Solution()
    input1 = "abcde"  # "1a1b1c1d1e"
    input2 = "aaaaaaaaaaaaaabb"  # "9a5a2b"
    print(sol.compressedString(input1))
    print(sol.compressedString(input2))
