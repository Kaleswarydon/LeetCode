from functools import cache

from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        @cache
        def dp(start):
            if start == len(s):
                return 0
            res = 1 + dp(start + 1)
            for end in range(start, len(s)):
                if s[start:end+1] in substr:
                    res = min(res, dp(end + 1))
            return res
        substr = set(dictionary)
        return dp(0)

if __name__ == '__main__':
    sol = Solution()
    input1 = "leetscode", ["leet","code","leetcode"]  # 1
    input2 = "sayhelloworld", ["hello","world"]  # 3
    print(sol.minExtraChar(*input1))
    print(sol.minExtraChar(*input2))
