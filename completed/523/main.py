from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def dummy(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        prefix_sum = 0
        x_prev = 0
        ht = defaultdict(lambda: -1)
        for i, x in enumerate(nums):
            if i and not x and not x_prev:
                return True
            x_prev = x
            p_prev = prefix_sum
            prefix_sum = (prefix_sum + x) % k
            if (not prefix_sum and i > 0) or -1 < ht[prefix_sum] < i - 1:
                return True
            else:
                if p_prev != prefix_sum:
                    ht[prefix_sum] = i
        return False



if __name__ == '__main__':
    sol = Solution()
    input1 = [23,2,4,6,7], 6 # True
    input2 = [23,2,6,4,7], 6 # True
    input3 = [23,2,6,4,7], 13 # False
    input4 = [23,2,4,6,6], 7 # True
    input5 = [1,0], 2 # False
    input6 = [0,1,0,3,0,4,0,4,0], 5 # False
    input7 = [2,4,3], 6 # True
    input8 = [5,0,0,0], 3 # True
    input9 = [1,3,0,6], 6 # True
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
    print(sol.dummy(*input3))
    print(sol.dummy(*input4))
    print(sol.dummy(*input5))
    print(sol.dummy(*input6))
    print(sol.dummy(*input7))
    print(sol.dummy(*input8))
    print(sol.dummy(*input9))
