from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def dummy(self, nums: List[int], k: int):
        prefix_dict = defaultdict(lambda: [])
        pref_sum = 0
        for i, x in enumerate(nums):
            pref_sum = (pref_sum + x) % k
            prefix_dict[pref_sum].append(i)
        res = 0
        for y in prefix_dict:
            n = len(prefix_dict.get(y))
            if not y or n > 1:
                res += ((n * (n + 1)) / 2)
                if y:
                    res -= n
        return int(res)


if __name__ == '__main__':
    sol = Solution()
    input1 = [4,5,0,-2,-3,1], 5 # 7
    input2 = [5], 9 # 0
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
