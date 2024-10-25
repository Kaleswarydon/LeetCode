from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def get_hist(s: str):
            h = [0] * 26
            for c in s:
                h[ord(c) - 97] += 1
            return h
        s1_h = get_hist(s1)
        curr_streak = 0
        for i in range(len(s2)):
            if s1_h[ord(s2[i]) - 97]:
                if curr_streak < len(s1):
                    curr_streak += 1
            else:
                curr_streak = 0
            if curr_streak >= len(s1) and get_hist(s2[max(0,i-(curr_streak-1)):i+1]) == s1_h:
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    input1 = "ab", "eidbaooo"  # True
    input2 = "ab", "eidboaoo"  # False
    input3 = "adc", "dcda"  # True
    print(sol.checkInclusion(*input1))
    print(sol.checkInclusion(*input2))
    print(sol.checkInclusion(*input3))
