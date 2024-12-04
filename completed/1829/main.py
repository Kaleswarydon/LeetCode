from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        r = [nums[0]]
        for i in range(1, len(nums)):
            r.append(r[-1] ^ nums[i])
        for j in range(len(nums)):
            r[j] ^= (2 ** maximumBit) - 1
        return r[::-1]

if __name__ == '__main__':
    sol = Solution()
    input1 = [0,1,1,3], 2  # [0,3,2,3]
    input2 = [2,3,4,7], 3  # [5,2,6,5]
    input3 = [0,1,2,2,5,7], 3  # [4,3,6,4,6,7]
    print(sol.getMaximumXor(*input1))
    print(sol.getMaximumXor(*input2))
    print(sol.getMaximumXor(*input3))
