from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        r = [0] * 24
        for i in range(24):
            for c in candidates:
                r[i] += int(bin(c)[2:].zfill(24)[i])
        return max(r)


if __name__ == '__main__':
    sol = Solution()
    input1 = [16,17,71,62,12,24,14]  # 4
    input2 = [8,8]  # 2
    print(sol.largestCombination(input1))
    print(sol.largestCombination(input2))
