from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        k -= 1
        curr_subtree = 1
        while k > 0:
            curr_subtree_tmp = curr_subtree
            next_subtree = curr_subtree + 1
            curr_subtree_node_count = 0
            while curr_subtree_tmp <= n:
                curr_subtree_node_count += min(next_subtree - curr_subtree_tmp, n - curr_subtree_tmp + 1)
                curr_subtree_tmp *= 10
                next_subtree *= 10
            if k >= curr_subtree_node_count:
                curr_subtree += 1
                k -= curr_subtree_node_count
            else:
                curr_subtree *= 10
                k -= 1
        return curr_subtree


if __name__ == '__main__':
    sol = Solution()
    input0 = 34, 15  # 22
    input1 = 13, 2  # 10
    input2 = 1, 1  # 1
    input3 = 10, 3  # 2
    input4 = 681692778, 351251360  # 416126219
    print(sol.findKthNumber(*input0))
    print(sol.findKthNumber(*input1))
    print(sol.findKthNumber(*input2))
    print(sol.findKthNumber(*input3))
    print(sol.findKthNumber(*input4))
