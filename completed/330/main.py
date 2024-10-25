from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def dummy(self, nums: List[int], n: int) -> int:
        res = 0
        reachable = 0
        nums = list(reversed(nums))
        while reachable < n:
            if nums and nums[-1] <= reachable + 1:
                reachable += nums[-1]
                nums.pop()
            else:
                reachable += reachable + 1
                res += 1
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = [1, 3], 6  # 1
    input2 = [1, 5, 10], 20  # 2
    input3 = [1, 2, 2], 5  # 0
    input4 = [1, 2, 31, 33], 2147483647  # 28
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
    print(sol.dummy(*input3))
    print(sol.dummy(*input4))
