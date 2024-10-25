from icecream import ic as print
from collections import defaultdict
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode

class Solution:
    def dummy(self, nums, k):
        if not k:
            return 0
        res = 0
        pointer_low = 0
        pointer_high = 0
        tmp = 1
        while pointer_high < len(nums):
            tmp *= nums[pointer_high]
            while tmp >= k and pointer_low <= pointer_high:
                tmp /= nums[pointer_low]
                pointer_low += 1
            res += pointer_high - pointer_low + 1
            pointer_high += 1
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = [10,5,2,6], 100 #8
    input2 = [1,2,3], 0 #0
    input3 = [1,1,1], 2 #6
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
    print(sol.dummy(*input3))
