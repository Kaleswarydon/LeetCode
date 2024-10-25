from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode

from itertools import combinations
class Solution:
    def dummy(self, nums):
        def subsets(l):
            for n in range(len(l) + 1):
                yield from combinations(l, n)
        def xor_on_iterable(l):
            if not l:
                return 0
            tmp = 0
            for x in l:
                tmp ^= x
            return tmp
        res = 0
        for s in subsets(nums):
            res += xor_on_iterable(s)
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = [1,3] #6
    input2 = [5,1,6] #20
    print(sol.dummy(input1))
    print(sol.dummy(input2))
