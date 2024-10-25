from icecream import ic as print
from collections import defaultdict
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode

class Solution:
    def dummy(self, nums, k):
        pointer_low = 0
        res = 0
        ht = defaultdict(lambda: 0)
        for pointer_high in range(len(nums)):
            ht[nums[pointer_high]] += 1
            while ht[nums[pointer_high]] > k and pointer_high > pointer_low:
                ht[nums[pointer_low]] -= 1
                pointer_low += 1
            tmp = pointer_high - pointer_low + 1
            if res < tmp:
                res = tmp
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = [1,2,3,1,2,3,1,2], 2 #6
    input2 = [1,2,1,2,1,2,1,2], 1 #2
    input3 = [5,5,5,5,5,5,5], 4 #4
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
    print(sol.dummy(*input3))
