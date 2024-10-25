from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode

class Solution:
    def dummy(self, nums):
        tmp = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            try:
                tmp[nums[i]] += 1
            except:
                tmp[-1] += 1
        tmp_sum = 0
        for j in range(len(tmp) - 1, -1, -1):
            tmp_sum += tmp[j]
            if tmp_sum == j:
                return tmp_sum
        return -1


if __name__ == '__main__':
    sol = Solution()
    input1 = [3,5] #2
    input2 = [0,0] #-1
    input3 = [0,4,3,0,4] #3
    print(sol.dummy(input1))
    print(sol.dummy(input2))
    print(sol.dummy(input3))
