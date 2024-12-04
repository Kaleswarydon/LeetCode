from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def get_next_chr(self, c, n):
        return chr((((ord(c) - 97) + n) % 26) + 97)
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i, j = 0, 0
        while i < len(str1) or j < len(str2):
            if str1[i] == str2[j] or \
                self.get_next_chr(str1[i], 1) == str2[j]:
                if j < len(str2) - 1:
                    j += 1
                else:
                    return True
            if i < len(str1) - 1:
                i += 1
            else:
                return False


if __name__ == '__main__':
    sol = Solution()
    input1 = "abc", "ad"  # true
    input2 = "zc", "ad"  # true
    input3 = "ab", "d"  # false
    print(sol.canMakeSubsequence(*input1))
    print(sol.canMakeSubsequence(*input2))
    print(sol.canMakeSubsequence(*input3))
