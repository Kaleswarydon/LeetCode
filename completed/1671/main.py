from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        inc = [-1] * len(nums)
        dec = [-1] * len(nums)
        for i in range(len(nums)):
            m_i = 0
            m_d = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    m_i = max(m_i, inc[j])
                if nums[len(nums) - 1 - j] < nums[len(nums) - 1 - i]:
                    m_d = max(m_d, dec[len(nums) - 1 - j])
            inc[i] = m_i + 1
            dec[len(nums) - 1 - i] = m_d + 1
        print(inc)
        print(dec)
        res = len(nums)
        for k in range(1, len(nums) - 1):
            if inc[k] > 1 and dec[k] > 1:
                res = min(res, len(nums) - inc[k] - dec[k] + 1)
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = [1,3,1]  # 0
    input2 = [2,1,1,5,6,2,3,1]  # 3
    input3 = [1,2,3,4,4,3,2,1]  # 1
    input4 = [1,16,84,9,29,71,86,79,72,12]  # 2
    input5 = [4,5,13,17,1,7,6,11,2,8,10,15,3,9,12,14,16]  # 10
    input6 = [100,92,89,77,74,66,64,66,64]  # 6
    print(sol.minimumMountainRemovals(input1))
    print(sol.minimumMountainRemovals(input2))
    print(sol.minimumMountainRemovals(input3))
    print(sol.minimumMountainRemovals(input4))
    print(sol.minimumMountainRemovals(input5))
    print(sol.minimumMountainRemovals(input6))
