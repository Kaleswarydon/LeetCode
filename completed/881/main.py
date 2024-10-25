from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode

class Solution:
    def dummy(self, people, limit):
        people.sort()
        ptr_hi = len(people) - 1
        ptr_lo = 0
        res = 0
        while ptr_lo <= ptr_hi:
            if people[ptr_lo] + people[ptr_hi] <= limit:
                ptr_lo += 1
            ptr_hi -= 1
            res += 1
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = [1,2], 3 #1
    input2 = [3,2,2,1], 3 #3
    input3 = [3,5,3,4], 5 #4
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
    print(sol.dummy(*input3))
