from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        for i in range(len(nums)):
            tmp = 0
            for j in range(i, len(nums)):
                tmp += nums[j]
                res.append(tmp)
        return sum(sorted(res)[left-1:right]) % ((10**9) + 7)


if __name__ == '__main__':
    sol = Solution()
    input1 = [1,2,3,4], 4, 1, 5  # 13
    input2 = [1,2,3,4], 4, 3, 4  # 6
    input3 = [1,2,3,4], 4, 1, 10  # 50
    print(sol.rangeSum(*input1))
    print(sol.rangeSum(*input2))
    print(sol.rangeSum(*input3))
