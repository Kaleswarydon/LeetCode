from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def minimumDeletions(self, s: str) -> int:
        occ = defaultdict(deque)
        a = 0
        b = 0
        for i in range(len(s)):
            occ[i].append(b)
            occ[len(s) - 1 - i].appendleft(a)
            if s[i] == 'b':
                b += 1
            if s[len(s) - 1 - i] == 'a':
                a += 1
        res = len(s)
        for j in range(len(s)):
            res = min(res, sum(occ[j]))
        return res


if __name__ == '__main__':
    sol = Solution()
    input1 = "aababbab"  # 2
    input2 = "bbaaaaabb"  # 2
    input3 = "baababbaabbaaabaabbabbbabaaaaaabaabababaaababbb"  # 18
    print(sol.minimumDeletions(input1))
    print(sol.minimumDeletions(input2))
    print(sol.minimumDeletions(input3))
