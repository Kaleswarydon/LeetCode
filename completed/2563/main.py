from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def binary_search(l, r, arr, target):
            while l <= r:
                m = (l + r) // 2
                if arr[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return r
        nums.sort()
        res = 0
        for i in range(len(nums)):
            lower_bound = lower - nums[i]
            upper_bound = upper - nums[i]
            range_lo = binary_search(i + 1, len(nums) - 1, nums, lower_bound)
            range_hi = binary_search(i + 1, len(nums) - 1, nums, upper_bound + 1)
            res += range_hi - range_lo
        return res


if __name__ == '__main__':
    sol = Solution()
    input1 = [0,1,7,4,4,5], 3, 6  # 6
    input2 = [1,7,9,2,5], 11, 11  # 1
    print(sol.countFairPairs(*input1))
    print(sol.countFairPairs(*input2))
