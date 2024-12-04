from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        for r in range(1, len(nums)):
            if nums[r-1] != nums[r] - 1:
                l = r
            if r >= k-1:
                if r - l + 1 < k:
                    res.append(-1)
                else:
                    res.append(nums[r])
        if k == 1:
            return nums
        return res


if __name__ == '__main__':
    sol = Solution()
    input1 = [1,2,3,4,3,2,5], 3  # [3,4,-1,-1,-1]
    input2 = [2,2,2,2,2], 4  # [-1,-1]
    input3 = [3,2,3,2,3,2], 2  # [-1,3,-1,3,-1]
    input4 = [1], 1  # [1]
    print(sol.resultsArray(*input1))
    print(sol.resultsArray(*input2))
    print(sol.resultsArray(*input3))
    print(sol.resultsArray(*input4))
