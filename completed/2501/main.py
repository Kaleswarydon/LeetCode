from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums_set = set(nums)
        memo = defaultdict(int)
        m = -1
        while nums_set:
            cntr = 1
            curr = nums_set.pop()
            if curr ** 2 in memo:
                memo[curr] += 1 + memo[curr ** 2]
            else:
                tmp = curr
                while tmp ** 2 in nums_set:
                    tmp = tmp ** 2
                    nums_set.remove(tmp)
                    cntr += 1
                memo[curr] = cntr + memo[tmp ** 2]
            m = max(m, memo[curr])
        return m if m > 1 else -1


if __name__ == '__main__':
    sol = Solution()
    input1 = [4,3,6,16,8,2]  # 3
    input2 = [2,3,5,6,7]  # -1
    input3 = [2,4,4,2]  # 2
    input4 = [2,4,8,16]  # 3
    print(sol.longestSquareStreak(input1))
    print(sol.longestSquareStreak(input2))
    print(sol.longestSquareStreak(input3))
    print(sol.longestSquareStreak(input4))
