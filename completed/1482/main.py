from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def is_day_possible(self, bloomDay, m, k, d):
        streak = 0
        bouquets_possible = 0
        for b in bloomDay:
            if b <= d:
                streak += 1
            else:
                bouquets_possible += streak // k
                streak = 0
        if not bouquets_possible or streak:
            bouquets_possible += streak // k
        if bouquets_possible >= m:
            return True
        return False

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        ptr_lo = min(bloomDay)
        ptr_hi = max(bloomDay)
        ptr_mi = ptr_hi
        while ptr_lo <= ptr_hi:
            tmp = self.is_day_possible(bloomDay, m, k, ptr_mi)
            if tmp:
                ptr_hi = ptr_mi - 1
            else:
                ptr_lo = ptr_mi + 1
            ptr_mi = (ptr_hi + ptr_lo) // 2
        return ptr_lo


if __name__ == '__main__':
    sol = Solution()
    input1 = [1,10,3,10,2], 3, 1  # 3
    input2 = [1,10,3,10,2], 3, 2  # -1
    input3 = [7,7,7,7,12,7,7], 2, 3  # 12
    input4 = [1000000000,1000000000], 1, 1  # 1000000000
    print(sol.minDays(*input1))
    print(sol.minDays(*input2))
    print(sol.minDays(*input3))
    print(sol.minDays(*input4))
