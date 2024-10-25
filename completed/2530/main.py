from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        res = 0
        for i in range(k):
            item = heapq.heappop(nums)
            res -= item
            heapq.heappush(nums, (item // 3))
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = [10,10,10,10,10], 5  # 50
    input2 = [1,10,3,3,3], 3  # 17
    print(sol.maxKelements(*input1))
    print(sol.maxKelements(*input2))
