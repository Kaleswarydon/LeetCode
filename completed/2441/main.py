from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode

class Solution:
    def dummy(self, nums):
        ht = defaultdict(lambda: 0)
        largest = -1
        for x in nums:
            if abs(x) > largest:
                if ht.get(x):
                    largest = abs(x)
                else:
                    ht[-x] = 1
        return largest

if __name__ == '__main__':
    sol = Solution()
    input1 = [-1,2,-3,3] #3
    input2 = [-1,10,6,7,-7,1] #7
    input3 = [-10,8,6,7,-2,-3] #-1
    print(sol.dummy(input1))
    print(sol.dummy(input2))
    print(sol.dummy(input3))
