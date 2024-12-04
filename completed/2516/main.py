from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        def check_valid(ss, kk):
            d = defaultdict(int)
            for c in ss:
                d[c] += 1
            return d if len(d.keys()) == 3 and all(d[h] >= kk for h in d.keys()) else None
        if not k:
            return 0
        freq_d = check_valid(s, k)
        if not freq_d:
            return -1
        res = len(s)
        j = 0
        for i in range(len(s)):
            while j < len(s) and freq_d[s[j]] > k:
                freq_d[s[j]] -= 1
                j += 1
            freq_d[s[i]] += 1
            #print(i, j, i + (len(s) - j))
            res = min(res, i + (len(s) - j))
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = "aabaaaacaabc", 2  # 8
    input2 = "a", 1  # -1
    input3 = "aabac", 1  # 3
    print(sol.takeCharacters(*input1))
    print(sol.takeCharacters(*input2))
    print(sol.takeCharacters(*input3))
