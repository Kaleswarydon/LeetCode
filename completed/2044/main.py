from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        m = 0
        for x in nums:
            m |= x
        res = 0
        for bm in range(1, 2 ** len(nums)):
            co = 0
            for i in range(len(nums)):
                if (1 << i) & bm:
                    co |= nums[i]
            if co == m:
                res += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    input1 = [3,1]  # 2
    input2 = [2,2,2]  # 7
    input3 = [3,2,1,5]  # 6
    print(sol.countMaxOrSubsets(input1))
    print(sol.countMaxOrSubsets(input2))
    print(sol.countMaxOrSubsets(input3))
