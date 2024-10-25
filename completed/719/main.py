from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def helper(k) -> int:
            n = len(nums) - 1
            i = 0
            while k - (n - i) > 0:
                k -= n - i
                i += 1
            return nums[k + i] - nums[k - 1]

        def count_pairs_up_to_dst(dst):
            amount = 0
            ptr_lo = 0
            for ptr_hi in range(len(nums)):
                while nums[ptr_hi] - nums[ptr_lo] > dst:
                    ptr_lo += 1
                amount += ptr_hi - ptr_lo
            return amount

        nums.sort()

        tmp = 0
        for i in range(len(nums) - 1):
            t = nums[i + 1] - nums[i]
            if t < tmp:
                l = 0
                r = max(nums)
                while l < r:
                    m = (l + r) // 2
                    p = count_pairs_up_to_dst(m)
                    if p >= k:
                        r = m
                    else:
                        l = m + 1
                return r
            tmp = t
        return helper(k)






if __name__ == '__main__':
    sol = Solution()
    input1 = [1,3,1], 1  # 0
    input2 = [1,1,1], 2  # 0
    input3 = [1,6,1], 3  # 5
    input4 = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900], 50
    print(sol.smallestDistancePair(*input1))
    print(sol.smallestDistancePair(*input2))
    print(sol.smallestDistancePair(*input3))
    print(sol.smallestDistancePair(*input4))
