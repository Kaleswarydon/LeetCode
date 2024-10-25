from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        val = nums[0]
        streak_current = 1
        streak_max = 1
        for i in range(1, len(nums)):
            if nums[i] == val:
                streak_current += 1
            elif nums[i] > val:
                val = nums[i]
                streak_current = 1
                streak_max = 1
            else:
                streak_max = max(streak_max, streak_current)
                streak_current = 0
        return max(streak_max, streak_current)

if __name__ == '__main__':
    sol = Solution()
    input1 = [1,2,3,3,2,2]  # 2
    input2 = [1,2,3,4]  # 1
    input3 = [311155,311155,311155,311155,311155,311155,311155,311155,201191,311155]  # 8
    input4 = [311155,311155,311155,311155,311155,311155,311155,311155,311155]  # 9
    print(sol.longestSubarray(input1))
    print(sol.longestSubarray(input2))
    print(sol.longestSubarray(input3))
    print(sol.longestSubarray(input4))
