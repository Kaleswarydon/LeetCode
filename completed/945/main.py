from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def dummy(self, nums):
        nums.sort()
        min_val = nums[0] - 1
        res = 0
        for x in nums:
            if x > min_val:
                min_val = x
            elif x == min_val:
                min_val += 1
                res += 1
            else:
                min_val += 1
                res += min_val - x
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = [1,2,2] # 1
    input2 = [3,2,1,2,1,7] # 6
    input3 = [1,1,1,2,2,3,4,5] # 17
    print(sol.dummy(input1))
    print(sol.dummy(input2))
    print(sol.dummy(input3))
