from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res = len(nums) + 1
        curr_sum = 0
        q = deque()
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum >= k:
                res = min(res, i + 1)
            curr = (float("-inf"), float("-inf"))
            while q and curr_sum - q[0][1] >= k:
                curr = q[0]
                q.popleft()
            if curr[1] != float("-inf"):
                res = min(res, i - curr[0])
            while q and curr_sum <= q[-1][1]:
                q.pop()
            q.append((i, curr_sum))
        if res == len(nums) + 1:
            return -1
        return res

if __name__ == '__main__':
    sol = Solution()
    input0 = [2,7,3,-8,4,10], 12  # 2
    input1 = [1], 1  # 1
    input2 = [1,2], 4  # -1
    input3 = [2,-1,2], 3  # 3
    input4 = [27,20,79,87,-36,78,76,72,50,-26], 453  # 9
    input5 = [-34,37,51,3,-12,-50,51,100,-47,99,34,14,-13,89,31,-14,-44,23,-38,6], 151  # 2
    print(sol.shortestSubarray(*input0))
    print(sol.shortestSubarray(*input1))
    print(sol.shortestSubarray(*input2))
    print(sol.shortestSubarray(*input3))
    print(sol.shortestSubarray(*input4))
    print(sol.shortestSubarray(*input5))
