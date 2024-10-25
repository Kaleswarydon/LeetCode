from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def is_possible(self, position, m, ptr_mi):
        placed_amount = 1  # first one is placed at position 0
        prev_pos = 0  # see above
        for i in range(1, len(position)):
            if position[i] - position[prev_pos] >= ptr_mi:
                prev_pos = i
                placed_amount += 1
        return m <= placed_amount

    def maxDistance(self, position: List[int], m: int) -> int:
        res = 0
        position.sort()
        ptr_lo = 0
        ptr_hi = position[-1]
        while ptr_lo <= ptr_hi:
            ptr_mi = (ptr_hi + ptr_lo) // 2
            tmp = self.is_possible(position, m, ptr_mi)
            if tmp:
                res = ptr_mi
                ptr_lo = ptr_mi + 1
            else:
                ptr_hi = ptr_mi - 1
        return res


if __name__ == '__main__':
    sol = Solution()
    input1 = [1,2,3,4,7], 3 # 3
    input2 = [5,4,3,2,1,1000000000], 2 # 999999999
    print(sol.maxDistance(*input1))
    print(sol.maxDistance(*input2))
