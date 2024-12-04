from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def count_bits(num: int):
            cntr = 0
            while num:
                num &= (num - 1)
                cntr += 1
            return cntr
        segments = [[-1, -1, 0, float("-inf")], [0, 0, nums[0], nums[0]]]
        curr_bits = count_bits(nums[0])
        for i, n in enumerate(nums[1:]):
            b = count_bits(n)
            if b == curr_bits:
                segments[-1][1] += 1
                segments[-1][2] = min(n, segments[-1][2])
                segments[-1][3] = max(n, segments[-1][3])
            else:
                if segments[-1][2] < segments[-2][3]:
                    return False
                new_seg = [i + 1, i + 1, n, n]
                segments.append(new_seg)
                curr_bits = b
        if segments[-1][2] < segments[-2][3]:
            return False
        return True

if __name__ == '__main__':
    sol = Solution()
    input1 = [8,4,2,30,15]  # True
    input2 = [1,2,3,4,5]  # True
    input3 = [3,16,8,4,2]  # False
    print(sol.canSortArray(input1))
    print(sol.canSortArray(input2))
    print(sol.canSortArray(input3))
