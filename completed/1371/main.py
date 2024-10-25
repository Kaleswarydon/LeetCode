from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        bm = defaultdict(int, {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16})
        if len(s) == 1:
            return int(s not in bm)
        dfault = [len(s), 0]
        streaks = defaultdict(lambda: dfault)
        streaks[0] = dfault
        current  = 0
        for i in range(len(s)):
            current ^= bm[s[i]]
            streaks[current] = [min(streaks[current][0], i + int(current != 0)), max(streaks[current][1], i)]
        res = 0
        print(streaks)
        for b in streaks:
            if streaks[b] != dfault:
                res = max(res, (max(streaks[b][1], int(b != 0) * (streaks[0][1] + 1)) - streaks[b][0]) + int(streaks[b][0] != streaks[b][1]))
        if not res and len(s):
            return len(s) - 1
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = "eleetminicoworoep"  # 13
    input2 = "leetcodeisgreat"  # 5
    input3 = "bcbcbc"  # 6
    input4 = "amntyyaw"  # 8
    input5 = "a"  # 0
    input6 = "z"  # 1
    input7 = "id"  # 1
    print(sol.findTheLongestSubstring(input1))
    print(sol.findTheLongestSubstring(input2))
    print(sol.findTheLongestSubstring(input3))
    print(sol.findTheLongestSubstring(input4))
    print(sol.findTheLongestSubstring(input5))
    print(sol.findTheLongestSubstring(input6))
    print(sol.findTheLongestSubstring(input7))
